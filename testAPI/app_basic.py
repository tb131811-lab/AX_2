"""증권사 홈 화면 스타일의 환율·시장 대시보드. 실행: streamlit run app_basic.py"""
import os
import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import parsedate_to_datetime
from html import escape

import requests
import streamlit as st
from dotenv import load_dotenv

ENV_PATH = r"C:\Users\user\AX_2\.env"
FX_URL = "https://v6.exchangerate-api.com/v6/{key}/latest/USD"
RSS = {
    "fx": "https://news.google.com/rss/search?q=%ED%99%98%EC%9C%A8+%EA%B2%BD%EC%A0%9C&hl=ko&gl=KR&ceid=KR:ko",
    "industry": "https://news.google.com/rss/search?q=%EC%82%B0%EC%97%85+%EB%B0%98%EB%8F%84%EC%B2%B4+%EB%B0%B0%ED%84%B0%EB%A6%AC+%EC%9E%90%EB%8F%99%EC%B0%A8&hl=ko&gl=KR&ceid=KR:ko",
}
FX_CARDS = {"KRW": ("USD / KRW", "₩", 2), "JPY": ("USD / JPY", "¥", 2), "EUR": ("EUR / USD", "€", 4), "CNY": ("USD / CNY", "¥", 4), "GBP": ("GBP / USD", "£", 4), "AUD": ("AUD / USD", "A$", 4)}
CURRENCIES = {"USD": "미국 달러", "KRW": "한국 원", "EUR": "유로", "JPY": "일본 엔", "CNY": "중국 위안", "GBP": "영국 파운드", "AUD": "호주 달러", "CAD": "캐나다 달러"}

load_dotenv(ENV_PATH)
st.set_page_config(page_title="Market Pulse | FX Dashboard", page_icon="📈", layout="wide")

@st.cache_data(ttl=300, show_spinner=False)
def fetch_rates(key):
    response = requests.get(FX_URL.format(key=key), timeout=10)
    response.raise_for_status()
    payload = response.json(); rates = payload.get("conversion_rates", {})
    if payload.get("result") != "success" or not rates: raise ValueError(payload.get("error-type", "환율 데이터를 불러오지 못했습니다."))
    return {k: float(v) for k, v in rates.items()}, payload.get("time_last_update_utc", "")

@st.cache_data(ttl=600, show_spinner=False)
def fetch_news(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10); response.raise_for_status()
    articles = []
    for item in ET.fromstring(response.content).findall("./channel/item")[:5]:
        published = item.findtext("pubDate", "")
        try: published = parsedate_to_datetime(published).astimezone().strftime("%m.%d %H:%M")
        except (TypeError, ValueError): pass
        articles.append((item.findtext("title", "제목 없음"), item.findtext("link", "#"), item.findtext("source", "경제 뉴스"), published))
    return articles

def pair_rate(code, rates): return 1 / rates[code] if code in {"EUR", "GBP", "AUD"} else rates[code]

def render_news(articles, message):
    if not articles: st.info(message); return
    for title, link, source, published in articles:
        st.markdown(f'<a class="news-card" href="{escape(link, quote=True)}" target="_blank" rel="noopener noreferrer"><div class="news-title">{escape(title)}</div><div class="news-meta">{escape(source)} <span>·</span> {escape(published)}</div></a>', unsafe_allow_html=True)

st.markdown("""<style>
.stApp{background:#f3f5f8;color:#1c2939}.block-container{max-width:1440px;padding:1.6rem 2.5rem 3rem}.market-header{display:flex;justify-content:space-between;align-items:center;padding:22px 28px;border-radius:14px;color:#fff;background:linear-gradient(110deg,#071934,#0a3b7d 68%,#146db4);box-shadow:0 10px 28px rgba(9,38,79,.18)}.market-header h1{margin:0;font-size:1.75rem;letter-spacing:-.7px}.market-header p{margin:6px 0 0;color:#bdd9ff;font-size:.9rem}.live{font-size:.78rem;border:1px solid #4d80bc;background:#082c62;border-radius:30px;padding:8px 12px;color:#e1efff}.section-title{font-size:1.08rem;font-weight:750;margin:24px 0 10px;color:#172b47}.section-sub{color:#78879a;font-size:.81rem;font-weight:400;margin-left:7px}div[data-testid="stMetric"]{background:#fff;border:1px solid #e0e6ee;border-radius:10px;padding:14px;box-shadow:0 2px 9px rgba(14,39,71,.035)}div[data-testid="stMetricLabel"]{color:#64748b;font-size:.8rem}div[data-testid="stMetricValue"]{font-size:1.35rem;color:#102b53}.news-card{display:block;text-decoration:none!important;color:#1b2b3e!important;padding:13px 0;border-bottom:1px solid #edf0f4}.news-card:last-child{border-bottom:0}.news-card:hover .news-title{color:#1264af}.news-title{font-size:.92rem;font-weight:650;line-height:1.43}.news-meta{color:#8491a2;font-size:.75rem;margin-top:6px}.news-meta span{margin:0 4px}.idea-panel{overflow:hidden;border-radius:13px;background:#071b39;color:#fff;box-shadow:0 10px 22px rgba(10,37,75,.18)}.idea-head{padding:18px 19px 15px;background:linear-gradient(115deg,#071932,#0c4c9b)}.idea-kicker{color:#75d8ff;font-size:.69rem;font-weight:800;letter-spacing:1.4px}.idea-head h2{margin:5px 0 5px;font-size:1.42rem;letter-spacing:-.7px;line-height:1.18;color:#fff}.idea-head p{margin:0;color:#c9e2ff;font-size:.78rem}.idea-list{padding:4px 17px 11px}.idea-item{display:flex;gap:11px;align-items:center;padding:11px 0;border-bottom:1px solid rgba(192,221,255,.16)}.idea-item:last-child{border-bottom:0}.idea-rank{flex:0 0 25px;width:25px;height:25px;border-radius:7px;background:#f4b41a;color:#08224b;font-size:.77rem;font-weight:900;text-align:center;line-height:25px}.idea-theme{font-size:.91rem;font-weight:800;letter-spacing:-.25px}.idea-stock{color:#9bc9ff;font-size:.74rem;margin-top:2px}.idea-tag{margin-left:auto;flex:0 0 auto;border:1px solid #4a82c4;border-radius:20px;padding:4px 7px;color:#d7edff;font-size:.65rem;font-weight:700}.idea-footer{padding:10px 17px 13px;background:rgba(255,255,255,.06);color:#afc7e8;font-size:.69rem}
</style>""", unsafe_allow_html=True)

now = datetime.now().strftime("%Y.%m.%d %H:%M")
st.markdown(f'<div class="market-header"><div><h1>MARKET PULSE</h1><p>환율 · 글로벌 증시 · 산업 동향을 한눈에</p></div><div class="live">● MARKET MONITORING&nbsp;&nbsp; {now}</div></div>', unsafe_allow_html=True)
rates = None; updated_at = ""; rate_error = None; key = os.getenv("EXCHANGERATE_API_KEY")
try:
    if not key: raise ValueError("EXCHANGERATE_API_KEY가 설정되지 않았습니다.")
    rates, updated_at = fetch_rates(key)
except (requests.RequestException, ValueError) as error: rate_error = str(error)

st.markdown('<div class="section-title">주요 환율 시세 <span class="section-sub">USD 기준</span></div>', unsafe_allow_html=True)
for col, (code, (label, symbol, decimals)) in zip(st.columns(6), FX_CARDS.items()):
    with col: st.metric(label, f"{symbol}{pair_rate(code, rates):,.{decimals}f}" if rates else "—", "업데이트된 기준가" if rates else "데이터 연결 대기")
if updated_at: st.caption(f"환율 기준 시각: {updated_at} · 제공: ExchangeRate-API")
elif rate_error: st.warning(f"환율 시세를 표시할 수 없습니다: {rate_error}")

st.markdown('<div class="section-title">환율 계산기</div>', unsafe_allow_html=True)
with st.container(border=True):
    a, b, c = st.columns([1.2, 1, 1])
    with a: amount = st.number_input("금액", min_value=0.0, value=1000.0, step=100.0, format="%.2f")
    with b: source = st.selectbox("보낼 통화", list(CURRENCIES), format_func=lambda x: f"{x} · {CURRENCIES[x]}")
    with c: target = st.selectbox("받을 통화", list(CURRENCIES), index=1, format_func=lambda x: f"{x} · {CURRENCIES[x]}")
    if rates:
        result = amount / rates[source] * rates[target]
        st.metric("환전 예상 금액", f"{result:,.2f} {target}", help="기준 환율 참고값입니다. 실제 환전에는 은행·증권사 환율과 수수료가 적용됩니다.")
        st.caption(f"1 {source} = {rates[target] / rates[source]:,.6f} {target}")
    else: st.info("환율 데이터를 받아오면 계산 결과가 표시됩니다.")

st.markdown('<div class="section-title">오늘의 투자 포커스 <span class="section-sub">테마 · 대표 관심 종목</span></div>', unsafe_allow_html=True)
st.markdown('''<div class="idea-panel"><div class="idea-head"><div class="idea-kicker">INVESTMENT RADAR</div><h2>돈이 몰리는 곳을 먼저 보세요.</h2><p>성장 동력과 실적 가시성을 함께 점검할 핵심 산업</p></div><div class="idea-list"><div class="idea-item"><div class="idea-rank">01</div><div><div class="idea-theme">AI 반도체 · HBM</div><div class="idea-stock">대표 관심 종목 · SK하이닉스 · NVIDIA</div></div><div class="idea-tag">성장 핵심</div></div><div class="idea-item"><div class="idea-rank">02</div><div><div class="idea-theme">전력 인프라 · 전력기기</div><div class="idea-stock">대표 관심 종목 · HD현대일렉트릭 · LS ELECTRIC</div></div><div class="idea-tag">수요 확대</div></div><div class="idea-item"><div class="idea-rank">03</div><div><div class="idea-theme">방산 · 수출 모멘텀</div><div class="idea-stock">대표 관심 종목 · 한화에어로스페이스 · LIG넥스원</div></div><div class="idea-tag">수주 주목</div></div></div><div class="idea-footer">종목 매수 전 밸류에이션 · 실적 · 변동성을 꼭 확인하세요.</div></div>''', unsafe_allow_html=True)

news_left, news_right = st.columns(2, gap="large")
with news_left:
    st.markdown('<div class="section-title">환율 · 경제 뉴스 <span class="section-sub">최신 기사</span></div>', unsafe_allow_html=True)
    with st.container(border=True):
        try: render_news(fetch_news(RSS["fx"]), "환율·경제 뉴스를 불러오지 못했습니다.")
        except (requests.RequestException, ET.ParseError): render_news([], "환율·경제 뉴스를 불러오지 못했습니다.")
with news_right:
    st.markdown('<div class="section-title">산업 동향 <span class="section-sub">반도체 · 배터리 · 모빌리티</span></div>', unsafe_allow_html=True)
    with st.container(border=True):
        try: render_news(fetch_news(RSS["industry"]), "산업 뉴스를 불러오지 못했습니다.")
        except (requests.RequestException, ET.ParseError): render_news([], "산업 뉴스를 불러오지 못했습니다.")
st.caption("투자 판단의 참고용 정보이며, 투자 권유 또는 금융상품 매매 제안이 아닙니다.")
