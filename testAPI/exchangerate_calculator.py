"""호환용 실행 진입점: 기존 파일명으로도 시장 대시보드를 엽니다."""
from app_basic import *  # noqa: F401,F403
st.stop()

import os

import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv


ENV_PATH = r"C:\Users\user\AX_2\.env"
EXCHANGE_RATE_URL = "https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"

CURRENCY_NAMES = {
    "USD": "미국 달러", "KRW": "대한민국 원", "EUR": "유로", "JPY": "일본 엔",
    "GBP": "영국 파운드", "CNY": "중국 위안", "HKD": "홍콩 달러", "SGD": "싱가포르 달러",
    "TWD": "대만 달러", "THB": "태국 바트", "INR": "인도 루피", "AUD": "호주 달러",
    "NZD": "뉴질랜드 달러", "CAD": "캐나다 달러", "CHF": "스위스 프랑",
    "SEK": "스웨덴 크로나", "NOK": "노르웨이 크로네", "DKK": "덴마크 크로네",
    "AED": "UAE 디르함", "SAR": "사우디 리얄", "ZAR": "남아프리카공화국 랜드",
    "MXN": "멕시코 페소", "BRL": "브라질 헤알",
}


@st.cache_data(ttl=1800, show_spinner=False)
def fetch_rates(api_key: str, base_currency: str) -> tuple[dict[str, float], str]:
    """기준 통화의 최신 환율과 갱신 시각을 가져온다."""
    response = requests.get(
        EXCHANGE_RATE_URL.format(api_key=api_key, base=base_currency), timeout=10
    )
    response.raise_for_status()
    data = response.json()
    rates = data.get("conversion_rates", {})
    if data.get("result") != "success" or not rates:
        raise ValueError(data.get("error-type", "환율 정보를 불러오지 못했습니다."))
    return {code: float(rate) for code, rate in rates.items()}, data.get(
        "time_last_update_utc", ""
    )


load_dotenv(ENV_PATH)
st.set_page_config(page_title="환율 계산기", page_icon="💱", layout="centered")
st.title("💱 환율 계산기")
st.caption("ExchangeRate-API의 최신 환율을 사용합니다.")

api_key = os.getenv("EXCHANGERATE_API_KEY")
if not api_key:
    st.error(".env 파일에 EXCHANGERATE_API_KEY를 설정해 주세요.")
    st.stop()

currency_codes = list(CURRENCY_NAMES)
options = [f"{code} · {CURRENCY_NAMES[code]}" for code in currency_codes]

amount_column, from_column, to_column = st.columns([1.2, 1, 1])
with amount_column:
    amount = st.number_input("금액", min_value=0.0, value=1.0, step=1.0, format="%.2f")
with from_column:
    from_option = st.selectbox("보낼 통화", options, index=0)
with to_column:
    to_option = st.selectbox("받을 통화", options, index=1)

from_currency = from_option[:3]
to_currency = to_option[:3]

try:
    with st.spinner("최신 환율을 불러오는 중입니다..."):
        rates, updated_at = fetch_rates(api_key, from_currency)
except requests.RequestException:
    st.error("환율 서버에 연결할 수 없습니다. 인터넷 연결과 API 키를 확인해 주세요.")
    st.stop()
except ValueError as error:
    st.error(f"환율 정보를 불러오지 못했습니다: {error}")
    st.stop()

if to_currency not in rates:
    st.error(f"{to_currency} 환율을 제공하지 않습니다.")
    st.stop()

converted_amount = amount * rates[to_currency]
st.metric(
    "환전 결과",
    f"{converted_amount:,.2f} {to_currency}",
    help=f"1 {from_currency} = {rates[to_currency]:,.6f} {to_currency}",
)
st.caption(f"1 {from_currency} = {rates[to_currency]:,.6f} {to_currency}")
if updated_at:
    st.caption(f"환율 기준 시각: {updated_at}")

st.divider()
st.subheader(f"1 {from_currency} 기준 주요 통화")
table_rows = [
    {
        "통화": f"{code} · {CURRENCY_NAMES[code]}",
        "환율": f"{rates[code]:,.6f}",
    }
    for code in currency_codes
    if code in rates
]
st.dataframe(pd.DataFrame(table_rows), width="stretch", hide_index=True)
