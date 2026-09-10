from pathlib import Path
import os
import requests
import pandas as pd
import streamlit as st
from dotenv import find_dotenv, load_dotenv

# 상위 폴더들을 탐색해 AX_2 루트의 .env 자동 로드
load_dotenv(find_dotenv())

CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
EXCHANGE_RATE_URL = "https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

# USD 기준 환율을 표시할 주요 국제 통화입니다.
MAJOR_CURRENCIES = {
    "KRW": "대한민국 원",
    "EUR": "유로",
    "JPY": "일본 엔",
    "GBP": "영국 파운드",
    "CNY": "중국 위안",
    "HKD": "홍콩 달러",
    "SGD": "싱가포르 달러",
    "TWD": "대만 달러",
    "THB": "태국 바트",
    "INR": "인도 루피",
    "AUD": "호주 달러",
    "NZD": "뉴질랜드 달러",
    "CAD": "캐나다 달러",
    "CHF": "스위스 프랑",
    "SEK": "스웨덴 크로나",
    "NOK": "노르웨이 크로네",
    "DKK": "덴마크 크로네",
    "AED": "UAE 디르함",
    "SAR": "사우디 리얄",
    "ZAR": "남아프리카공화국 랜드",
    "MXN": "멕시코 페소",
    "BRL": "브라질 헤알",
}


@st.cache_data(ttl=600, show_spinner=False)
def fetch_weather(city: str, api_key: str) -> tuple[dict, dict]:
    """현재 날씨와 5일 예보를 OpenWeatherMap에서 가져온다."""
    params = {"q": city, "appid": api_key, "units": "metric", "lang": "kr"}
    current = requests.get(CURRENT_WEATHER_URL, params=params, timeout=10)
    forecast = requests.get(FORECAST_URL, params=params, timeout=10)
    current.raise_for_status()
    forecast.raise_for_status()
    return current.json(), forecast.json()


@st.cache_data(ttl=1800, show_spinner=False)
def fetch_exchange_rates(api_key: str) -> dict[str, float]:
    """ExchangeRate-API에서 미국 달러 기준 국제 통화 환율을 가져온다."""
    response = requests.get(
        EXCHANGE_RATE_URL.format(api_key=api_key), timeout=10
    )
    response.raise_for_status()
    data = response.json()
    if data.get("result") != "success" or "KRW" not in data.get("conversion_rates", {}):
        raise ValueError(data.get("error-type", "환율 정보를 가져오지 못했습니다."))
    return {
        currency: float(rate)
        for currency, rate in data["conversion_rates"].items()
    }


def weather_icon(icon_code: str) -> str:
    """OpenWeatherMap 아이콘 코드에 대응하는 이모지."""
    return {
        "01": "☀️", "02": "🌤️", "03": "☁️", "04": "☁️",
        "09": "🌧️", "10": "🌦️", "11": "⛈️", "13": "❄️", "50": "🌫️",
    }.get(icon_code[:2], "🌡️")


st.set_page_config(page_title="오늘의 날씨", page_icon="🌤️", layout="centered")
st.title("🌤️ 오늘의 날씨")
st.caption("도시를 검색해 현재 날씨와 5일 예보를 확인하세요.")

api_key = os.getenv("OPENWEATHER_API_KEY")
exchange_rate_api_key = os.getenv("EXCHANGERATE_API_KEY")
if not api_key:
    st.error("OPENWEATHER_API_KEY를 AX_2 루트의 .env 파일에 설정해 주세요.")
    st.code("OPENWEATHER_API_KEY=발급받은_API_키", language="text")
    st.stop()

with st.form("weather_search"):
    city = st.text_input("도시", value="Seoul", placeholder="예: Seoul, Busan, Tokyo")
    submitted = st.form_submit_button("날씨 조회", type="primary")

if submitted:
    clean_city = city.strip()
    if not clean_city:
        st.warning("도시 이름을 입력해 주세요.")
        st.stop()

    try:
        with st.spinner("날씨 정보를 불러오는 중입니다..."):
            current, forecast = fetch_weather(clean_city.title(), api_key)
    except requests.HTTPError as error:
        if error.response.status_code == 401:
            st.error("API 키가 유효하지 않습니다. .env 설정을 확인해 주세요.")
        elif error.response.status_code == 404:
            st.error("해당 도시를 찾을 수 없습니다. 영문 도시명으로 다시 입력해 보세요.")
        else:
            st.error(f"날씨 정보를 가져오지 못했습니다. (HTTP {error.response.status_code})")
        st.stop()
    except requests.RequestException:
        st.error("네트워크 연결을 확인한 뒤 다시 시도해 주세요.")
        st.stop()

    exchange_rates = None
    if exchange_rate_api_key:
        try:
            exchange_rates = fetch_exchange_rates(exchange_rate_api_key)
        except (requests.RequestException, ValueError):
            st.warning("환율 정보를 지금 불러오지 못했습니다.")

    usd_krw_rate = exchange_rates.get("KRW") if exchange_rates else None
    details = current["weather"][0]
    main = current["main"]
    coord = current["coord"]

    weather_column, exchange_column = st.columns([3, 1])
    with weather_column:
        st.subheader(f"{current['name']}, {current['sys']['country']}")
        left, middle, right = st.columns(3)
        left.metric("현재 기온", f"{main['temp']:.1f} °C")
        middle.metric("체감 온도", f"{main['feels_like']:.1f} °C")
        right.metric("습도", f"{main['humidity']}%")
        st.markdown(
            f"**{weather_icon(details['icon'])} {details['description'].capitalize()}**  \n"
            f"최저 {main['temp_min']:.1f} °C · 최고 {main['temp_max']:.1f} °C · "
            f"풍속 {current['wind']['speed']:.1f} m/s"
        )
    with exchange_column:
        st.subheader("환율")
        if usd_krw_rate is not None:
            st.metric("미국 달러 (USD)", f"₩{usd_krw_rate:,.2f}", help="1 USD 기준 KRW 환율")
            st.caption("1 USD 기준 · ExchangeRate-API")
        else:
            st.info("환율 정보를 사용할 수 없습니다.")

    if exchange_rates:
        st.divider()
        st.subheader("주요 국제 통화 환율")
        st.caption("1 USD 기준 · ExchangeRate-API")
        rate_rows = [
            {
                "통화": f"{code} · {name}",
                "환율": f"{exchange_rates[code]:,.4f}",
            }
            for code, name in MAJOR_CURRENCIES.items()
            if code in exchange_rates
        ]
        st.dataframe(rate_rows, width="stretch", hide_index=True)

    st.divider()
    st.subheader("📍 위치 지도")
    map_data = pd.DataFrame([{"lat": coord["lat"], "lon": coord["lon"]}])
    st.map(map_data, zoom=10)

    st.divider()
    st.subheader("3시간 단위 예보")
    forecast_rows = []
    for item in forecast["list"][:8]:
        item_weather = item["weather"][0]
        forecast_rows.append({
            "시간": item["dt_txt"][5:16],
            "날씨": f"{weather_icon(item_weather['icon'])} {item_weather['description']}",
            "기온 (°C)": round(item["main"]["temp"], 1),
            "습도 (%)": item["main"]["humidity"],
        })
    st.dataframe(forecast_rows, width="stretch", hide_index=True)
else:
    st.info("도시를 입력하고 ‘날씨 조회’를 눌러 주세요.")
