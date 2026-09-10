import streamlit as st

st.set_page_config(
    page_title="도파민 폭발! 글로벌 무역 T-MBTI 파인더",
    page_icon="🚢",
    layout="wide"
)

# 화사하고 가독성 극대화된 프리미엄 라이트 테마 CSS
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif; }

    /* 기본 배경 */
    .stApp {
        background-color: #F8FAFC !important;
        color: #1E293B !important;
    }
    
    /* 인트로 히어로 배너 */
    .intro-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 24px;
        padding: 4rem 2rem;
        text-align: center;
        margin: 2rem auto;
        max-width: 860px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    }
    .intro-badge {
        display: inline-block;
        background: #EEF2FF;
        color: #4F46E5;
        border: 1px solid #C7D2FE;
        font-weight: 800;
        font-size: 0.9rem;
        padding: 0.4rem 1.2rem;
        border-radius: 9999px;
        letter-spacing: 0.06em;
        margin-bottom: 1.2rem;
    }
    .intro-title {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 50%, #6366F1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.2rem;
        line-height: 1.25;
    }
    .intro-desc {
        color: #475569;
        font-size: 1.15rem;
        line-height: 1.8;
        max-width: 720px;
        margin: 0 auto 2rem auto;
    }

    /* 🔥 질문 카드 스타일: 화면 중앙 집중형 */
    .q-card {
        background: #FFFFFF;
        border: 1.5px solid #E2E8F0;
        border-radius: 18px;
        padding: 1.6rem 1.8rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
        transition: all 0.2s ease;
    }
    .q-card:hover {
        border-color: #93C5FD;
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.08);
    }
    .q-header-row {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.7rem;
    }
    .q-icon-avatar {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 44px;
        height: 44px;
        background: #EFF6FF;
        border: 1.5px solid #BFDBFE;
        border-radius: 12px;
        font-size: 1.5rem;
        box-shadow: 0 2px 6px rgba(37, 99, 235, 0.08);
        flex-shrink: 0;
    }
    .q-badge {
        display: inline-block;
        font-size: 0.8rem;
        font-weight: 800;
        letter-spacing: 0.06em;
        color: #2563EB;
        background: #EFF6FF;
        border: 1px solid #BFDBFE;
        padding: 0.25rem 0.8rem;
        border-radius: 6px;
    }
    .q-tag-text {
        font-size: 0.82rem;
        font-weight: 700;
        color: #64748B;
    }
    .q-title {
        font-size: 1.22rem;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.6;
        margin-bottom: 0.4rem;
        word-break: keep-all;
    }

    /* 보기 선택지 카드 버튼 커스텀 */
    div[role="radiogroup"] {
        display: flex;
        flex-direction: column;
        gap: 0.9rem;
        margin-top: 0.8rem;
    }
    div[role="radiogroup"] > label {
        background: #FFFFFF !important;
        border: 1.8px solid #E2E8F0 !important;
        border-radius: 14px !important;
        padding: 1.1rem 1.5rem !important;
        cursor: pointer !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03) !important;
        transform: scale(1);
    }
    div[role="radiogroup"] > label:hover {
        border-color: #3B82F6 !important;
        background: #F0F7FF !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(37, 99, 235, 0.12) !important;
    }
    div[role="radiogroup"] > label:has(input:checked) {
        border-color: #2563EB !important;
        background: #EFF6FF !important;
        box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2), 0 8px 20px rgba(37, 99, 235, 0.12) !important;
        transform: scale(1.008) !important;
    }
    div[role="radiogroup"] > label p {
        font-size: 1.08rem !important;
        font-weight: 600 !important;
        color: #334155 !important;
        line-height: 1.55 !important;
    }
    div[role="radiogroup"] > label:has(input:checked) p {
        color: #1D4ED8 !important;
        font-weight: 800 !important;
    }

    /* 결과 대시보드 상단 배너 */
    .dash-hero {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        border-radius: 22px;
        padding: 2.5rem 2rem;
        text-align: center;
        box-shadow: 0 16px 36px rgba(15, 23, 42, 0.15);
        margin-bottom: 1.5rem;
    }
    .type-compare-container {
        display: flex;
        justify-content: center;
        align-items: stretch;
        gap: 1.5rem;
        margin: 1.5rem 0 1.8rem 0;
        flex-wrap: wrap;
    }
    .type-pill {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.16);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        flex: 1;
        min-width: 280px;
        max-width: 480px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .type-pill-title {
        font-size: 0.92rem;
        font-weight: 800;
        letter-spacing: 0.05em;
        color: #93C5FD;
        margin-bottom: 0.4rem;
    }
    .type-pill-val-trade {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(90deg, #F43F5E, #FB7185);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 0.05em;
    }
    .type-pill-val-real {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(90deg, #38BDF8, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 0.05em;
    }

    /* 초대형 단점 경고 전광판 카드 */
    .fault-fix-mega-box {
        background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
        border: 2.5px solid #EF4444;
        border-radius: 18px;
        padding: 1.8rem 2.2rem;
        margin-top: 1.6rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(239, 68, 68, 0.2);
    }
    .fault-fix-badge {
        display: inline-block;
        background: #DC2626;
        color: #FFFFFF;
        font-size: 0.95rem;
        font-weight: 900;
        letter-spacing: 0.08em;
        padding: 0.45rem 1.4rem;
        border-radius: 9999px;
        margin-bottom: 0.9rem;
        box-shadow: 0 4px 12px rgba(220, 38, 38, 0.3);
    }
    .fault-fix-mega-text {
        color: #991B1B;
        font-size: 1.45rem;
        font-weight: 850;
        line-height: 1.65;
        word-break: keep-all;
    }

    /* 대시보드 하단 화이트 패널 */
    .dash-panel {
        background: #FFFFFF;
        border: 1.5px solid #E2E8F0;
        border-radius: 18px;
        padding: 1.8rem;
        height: 100%;
        box-shadow: 0 4px 18px rgba(0, 0, 0, 0.04);
    }
    .dash-panel h3 {
        font-size: 1.25rem;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 1rem;
    }
    .skill-chip {
        display: inline-block;
        background: #EFF6FF;
        border: 1px solid #BFDBFE;
        color: #1D4ED8;
        font-size: 0.9rem;
        font-weight: 700;
        padding: 0.45rem 0.9rem;
        border-radius: 8px;
        margin: 0.25rem 0.35rem 0.25rem 0;
    }
    .rr-item {
        background: #F8FAFC;
        border-left: 4px solid #2563EB;
        padding: 0.85rem 1.1rem;
        border-radius: 0 10px 10px 0;
        margin-bottom: 0.65rem;
        font-size: 0.98rem;
        color: #334155;
        line-height: 1.55;
        border-top: 1px solid #F1F5F9;
        border-right: 1px solid #F1F5F9;
        border-bottom: 1px solid #F1F5F9;
    }
</style>
""", unsafe_allow_html=True)

# 각 질문별 맞춤 이모티콘 및 태그가 결합된 20개 시나리오 리스트[cite: 7, 8]
QUESTIONS = [
    # STEP 1 (Q1~Q4)[cite: 7, 8]
    {
        "id": 1,
        "icon": "🥂",
        "tag": "VIP 샴페인 네고",
        "q": "해외 엑스포 VIP 애프터 파티, 샴페인 병나발 불고 있는 거대 유통 재벌 회장과 정면으로 눈이 마주쳤다!",
        "options": [
            ("E", "눈 마주치자마자 윙크 박고 샷잔 들고 돌진! K-원샷 파도타기로 회장님 어깨동무하고 인맥 딴다."),
            ("I", "기둥 뒤에 은폐 엄폐! 휴대폰 쥔 채 회장 전용기 기종과 M&A 기사 구글링하며 결정적 순간만 노린다.")
        ]
    },
    {
        "id": 2,
        "icon": "🔬",
        "tag": "0.3mm 불량 분쟁",
        "q": "베트남 공장에서 보낸 10만 개 초도 물량 샘플을 깠는데, 로고 각인이 미세하게 삐뚤어져 있다!",
        "options": [
            ("S", "현미경과 버니어캘리퍼스 꺼내 오차 0.3mm 칼측정 후 계약서 스펙 조항에 빨간 펜 난사한다."),
            ("N", "'이거 단순 불량 맞아? 공장장이 뒷돈 챙기고 짝퉁 틀 돌린 거 아냐?' 공급망 마피아 시나리오 집필한다.")
        ]
    },
    {
        "id": 3,
        "icon": "🐶",
        "tag": "100억 계약 vs 반려견",
        "q": "100억짜리 독점 공급 도장 찍기 10분 전, 바이어가 \"우리 집 강아지가 위독해서 계약을 멈추겠다\"며 대성통곡한다.",
        "options": [
            ("T", "\"반려견의 쾌유를 빕니다만, 금일 18시 이후 원자재 폭등으로 계약금 15% 인상됩니다.\" 계약서 내민다."),
            ("F", "\"강아지도 엄연한 가족이죠... 얼마나 찢어지실까\" 같이 눈물 콧물 흘리며 계약 연기 서약서 써준다.")
        ]
    },
    {
        "id": 4,
        "icon": "🌪️",
        "tag": "태풍 상륙 & 결항 비상",
        "q": "선적 마감(Closing) 3시간 전! 초대형 태풍 상륙으로 항만이 셧다운되고 배가 결항 직전이다!",
        "options": [
            ("J", "선사 본사에 전화 100통 때려 대체 피더선 잡고, 항공 특송(Air Cargo) 화물기 자리까지 플랜 B로 선점한다."),
            ("P", "\"인간이 태풍을 어찌 이겨! 하늘의 뜻이다!\" 소주 한잔 마시고 내일 태풍 경로 바뀌길 기도하며 잔다.")
        ]
    },

    # STEP 2 (Q5~Q8)[cite: 7, 8]
    {
        "id": 5,
        "icon": "📢",
        "tag": "CES 라스베이거스 인파",
        "q": "CES 라스베이거스 부스 앞 복도에 전 세계 인플루언서와 취재진 수백 명이 벌떼처럼 몰려왔다!",
        "options": [
            ("E", "확성기 켜고 부스 위로 뛰어올라 미친 텐션으로 샘플 뿌리며 바이럴 스타가 된다."),
            ("I", "부스 백월 안쪽에 숨어 숨죽인 채, 명함 정리와 바이어 인콰이어리 DB만 묵묵히 입력한다.")
        ]
    },
    {
        "id": 6,
        "icon": "🩸",
        "tag": "부산 신항만 봉인 씰",
        "q": "부산 신항만 부두 바닥에서 핏자국 같은 붉은 페인트가 묻은 낡은 컨테이너 봉인 씰(Seal)을 주웠다!",
        "options": [
            ("S", "\"고유 번호 6자리 영문 스틸 규격이네. 터미널 하역 충격으로 파손된 철제 부속일 뿐.\""),
            ("N", "\"밀수 컨테이너에서 암시장 조직원들이 혈투를 벌이고 흘린 복선의 전리품 아닐까?!\"")
        ]
    },
    {
        "id": 7,
        "icon": "💸",
        "tag": "50억 계약서 환율 펑크",
        "q": "피땀 흘려 며칠 밤샌 사수의 50억짜리 수출 계약서에서 회사가 파산할 치명적인 환율 수식 오류를 발견했다!",
        "options": [
            ("T", "\"선배님, 3조 2항 환율 수식 펑크로 20억 증발합니다. 지금 당장 빨간 줄 긋고 고치겠습니다.\""),
            ("F", "\"선배님 며칠 밤새워서 뇌 과부하 오셨나 봐요 ㅠㅠ 감쪽같이 수정해 둘 테니 모른 척하세요!\"")
        ]
    },
    {
        "id": 8,
        "icon": "🚂",
        "tag": "시베리아 설원 횡단 철도",
        "q": "수에즈 운하 침몰 사고로 뱃길이 올스톱! 선사가 \"시베리아 횡단 야간 밀항 철도 우회로\"를 제안한다.",
        "options": [
            ("J", "시베리아 설원에서 분실되면 회사 망한다. 돈 3배 들더라도 검증된 희망봉 우회 항로로 보낸다."),
            ("P", "\"시베리아 설원 횡단 특급열차?! 개도파민 터지네! 사나이 가는 길 신항로 개척이다!\" 바로 태운다.")
        ]
    },

    # STEP 3 (Q9~Q12)[cite: 7, 8]
    {
        "id": 9,
        "icon": "🐊",
        "tag": "아프리카 오지 악어주",
        "q": "아프리카 오지 출장길, 바이어가 악어 쓸개즙에 현지 독주를 섞은 지독한 폭탄주를 대접하며 계약주라고 내민다.",
        "options": [
            ("E", "\"원샷 노 브레이크!\" 괴성 지르며 목구멍에 들이붓고 바이어와 춤추며 계약서 도장 찍는다."),
            ("I", "\"제가 종교적 신념으로 금주 중이라...\" 땀 뻘뻘 흘리며 정중히 거절하고 챙겨온 생수를 마신다.")
        ]
    },
    {
        "id": 10,
        "icon": "📈",
        "tag": "원자재 구리 시세 급등",
        "q": "원자재 구리(Copper) 가격이 10년 만에 폭등하며 글로벌 공장들이 연쇄 셧다운 중이라는 속보가 떴다!",
        "options": [
            ("S", "런던금속거래소(LME) 실시간 호가창 띄워놓고 우리 제품 1개당 원가 42원 상승치부터 엑셀로 두드린다."),
            ("N", "'구리가 폭망하면 전기차 배터리가 멈추고 인류 문명이 원시 시대로 퇴보하나?' 디스토피아를 그린다.")
        ]
    },
    {
        "id": 11,
        "icon": "🔥",
        "tag": "바이어 방화 협박",
        "q": "선적 3일 늦었다고 미쳐 날뛰는 외국 바이어가 \"물건값 30% 안 깎아주면 한국 대사관에 불 지르겠다\"고 협박한다.",
        "options": [
            ("T", "인코텀즈 면책 규정과 살인적 위약벌 법조항을 낭독하며 \"법정 갈 준비나 하라\"고 맞불을 놓는다."),
            ("F", "\"사장님 뒷목 잡으신 거 백번 이해합니다 ㅠㅠ 진정하시고 다음 발주 때 무료 사은품 폭탄 어떠세요?\"")
        ]
    },
    {
        "id": 12,
        "icon": "💻",
        "tag": "바탕화면 아수라장",
        "q": "내 무역 업무용 노트북 바탕화면과 B/L(선하증권) 서류 보관 폴더의 실제 상태는?",
        "options": [
            ("J", "연도 > 대륙 > 국가 > 바이어코드 > 선적주차별로 1mm 오차도 없이 칼각 정리되어 있음."),
            ("P", "바탕화면에 '최종_진짜마지막_제발_최최종_수정본.pdf'와 스크린샷 수백 개가 도배된 아수라장.")
        ]
    },

    # STEP 4 (Q13~Q16)[cite: 7, 8]
    {
        "id": 13,
        "icon": "🕺",
        "tag": "1억 빵 광란 댄스 배틀",
        "q": "글로벌 상사 연합 워크숍 뒤풀이 노래방에서 '글로벌 광란의 댄스 배틀 1억 빵'이 열렸다!",
        "options": [
            ("E", "넥타이 머리에 두르고 테이블 위로 올라가 트월킹 갈기며 전 세계 주재원들을 압살한다."),
            ("I", "비상구 옆 어두운 구석에 웅크려 탬버린만 박자에 맞춰 흔들며 화장실 핑계로 탈출 각을 잰다.")
        ]
    },
    {
        "id": 14,
        "icon": "👓",
        "tag": "5달러 통역 안경 직구",
        "q": "해외 직구 사이트에서 '단돈 5달러짜리 스마트폰 자동 통역 안경'이라는 미친 괴작을 발견했다!",
        "options": [
            ("S", "KC전파인증 통과 여부, 배터리 용량, 관세율표 9004호 품목분류 세금부터 냉정하게 계산한다."),
            ("N", "'이거 독점 수입해서 전 세계 언어 장벽 무너뜨리고 세계 평화의 아이콘이 되는 빅픽처?!'")
        ]
    },
    {
        "id": 15,
        "icon": "💥",
        "tag": "30억 신용장 도장 거절",
        "q": "신입사원이 L/C(신용장) 서류에 도장을 거꾸로 찍어 은행에서 30억 결제 거절당하고 바닥에 주저앉아 오열한다.",
        "options": [
            ("T", "\"질질 짤 시간에 스위프트(SWIFT) 전신 수정 요청 전문이나 쳐. 10분 늦으면 30억 부도야.\""),
            ("F", "\"야야 안 죽어! 괜찮아 나도 옛날에 날려먹었어! 심호흡하고 사수 형 믿고 따라와!\"")
        ]
    },
    {
        "id": 16,
        "icon": "🧳",
        "tag": "이륙 2시간 전 캐리어",
        "q": "비행기 이륙 2시간 전! 당장 공항 리무진을 타야 하는데 내 출장 캐리어의 상태는?",
        "options": [
            ("J", "바이어 선물, 샘플 키트, 어댑터, 비상약이 라벨링 지퍼백에 3중 방수 패킹되어 완벽 밀봉됨."),
            ("P", "\"여권이랑 회사 법인카드만 있으면 전 세계 어디서든 살아남아!\" 옷장 속 옷 몇 벌 쑤셔 넣고 닫음.")
        ]
    },

    # STEP 5 (Q17~Q20)[cite: 7, 8]
    {
        "id": 17,
        "icon": "👑",
        "tag": "중동 오일 거물과의 만남",
        "q": "유럽 공항 환승 대기 8시간 지옥, 옆자리에 롤렉스를 차고 지루해 보이는 중동 오일머니 거물이 앉아있다.",
        "options": [
            ("E", "커피 두 잔 뽑아 들고 \"헤이 브라더! 비즈니스 토크 좀 할까?\" 바로 옆자리 침투해 말문 튼다."),
            ("I", "노이즈 캔슬링 켜고 모자 푹 눌러쓴 뒤, 먼발치에서 가자미눈으로 오일 거물의 명품 시계만 훔쳐본다.")
        ]
    },
    {
        "id": 18,
        "icon": "🍿",
        "tag": "K-스낵 바이어 브리핑",
        "q": "유럽 바이어가 \"요즘 서울에서 20대가 열광하는 K-스낵 트렌드를 브리핑해달라\"고 긴급 요청했다.",
        "options": [
            ("S", "편의점 POS기 판매 데이터 탑5, 당도(Brix), 1봉당 수출 단가 실측 팩트 시트를 보낸다."),
            ("N", "'K-팝 아이돌의 영혼을 위로하는 심야의 도파민 폭탄'을 콘셉트로 몽환적인 감성 기획서를 쏜다.")
        ]
    },
    {
        "id": 19,
        "icon": "⏰",
        "tag": "시차 핑계와 딜레이 클레임",
        "q": "팀 프로젝트 조원이 \"유럽 바이어 시차 맞춘다고 새벽 4시까지 깨어있다 늦잠 자서 계약 딜레이됐다\"고 핑계 댈 때",
        "options": [
            ("T", "\"시차 핑계 대지 마. 알람을 10개 맞췄어야지. 펑크 난 지체보상금 네 월급에서 깔 거냐?\""),
            ("F", "\"새벽까지 잠도 못 자고 얼마나 몸이 갈렸겠어 ㅠㅠ 몸은 괜찮아? 남은 건 내가 수습할게.\"")
        ]
    },
    {
        "id": 20,
        "icon": "🏜️",
        "tag": "두바이 사막 사파리 질주",
        "q": "두바이 출장 마지막 날, 까다로운 바이어와의 미팅이 대성공으로 끝나 황금 같은 반나절 자유시간이 생겼다!",
        "options": [
            ("J", "출국 전 분 단위로 짜둔 '두바이 랜드마크 & B2B 메가몰 5대 스팟'을 엑셀 일정표대로 정복한다."),
            ("P", "\"소리 질러 자유다!\" 발길 닿는 대로 사막 사파리 지프차에 몸 싣고 도파민 폭주 레이싱을 즐긴다.")
        ]
    }
]

# T-MBTI 축 매핑[cite: 7, 8]
TRADE_AXIS = {
    "E": ("F", "Frontier (글로벌 개척형)"),
    "I": ("B", "Backbone (내부 수호형)"),
    "S": ("D", "Detail (정밀 검증형)"),
    "N": ("V", "Vision (전략 기획형)"),
    "T": ("N", "Nego (냉철 협상형)"),
    "F": ("R", "Relation (신뢰 관계형)"),
    "J": ("S", "System (원칙 통제형)"),
    "P": ("A", "Agile (유연 기동형)")
}

# 16개 MBTI별 단점 및 팩폭 피드백[cite: 7, 8]
MBTI_FAULT_FIX = {
    "ENTP": "말만 번지르르하게 100개 판 벌려놓고 뒷감당 서류는 팀원한테 짬때리지 마라. 수습 안 하면 횡령/배임 엔딩이다.",
    "ESTP": "현장 감각 좋다고 계약서 잉크도 마르기 전에 오랄(구두)로 딜 확정짓지 마라. 녹취 없으면 네가 다 물어낸다.",
    "ENTJ": "부하직원 숨 막히게 쥐어짜며 군대식 돌격하지 마라. 네 밑에 애들 다 퇴사해서 선적 서류 네가 밤새 쳐야 한다.",
    "ENFP": "박람회에서 바이어랑 베프 먹고 감정에 취해 노마진으로 퍼주지 마라. 회사는 자선사업 단체가 아니다.",
    "ENFJ": "모두에게 착한 사람 되려다 거래처 갑질과 무리한 단가 인하 요구 다 받아주지 마라. 호구 잡히면 끝이다.",
    "ESFP": "출장 가서 바이어 접대 파티하느라 다음 날 공식 협상 테이블에 지각하지 마라. 한 방에 딜 깨진다.",
    "ESFJ": "바이어 기분 맞춰주느라 원칙에도 없는 납기 단축 구두 약속 남발하지 마라. 공장장한테 멱살 잡힌다.",
    "ISTJ": "법률 규정 따지느라 골든타임 다 놓치지 마라. 규정은 100점인데 바이어는 이미 경쟁사로 떠났다.",
    "ESTJ": "내 방식만 맞다고 고집부리며 파트너사 포워더 쥐잡듯 잡지 마라. 물류 대란 터지면 아무도 네 화물 안 실어준다.",
    "ISFJ": "거절 못 해서 남의 똥 치우느라 새벽 야근하지 마라. 착한 척하다 정작 네 담당 선적 스케줄 펑크 난다.",
    "ISFP": "갈등 생겼다고 카톡/메일 읽씹하고 동굴로 도망치지 마라. 무역 클레임은 회피할수록 배상금에 복리 붙는다.",
    "INTJ": "남들 다 멍청해 보인다고 혼자 독단으로 결재 올리지 마라. 세상은 네 엑셀 시트대로 안 돌아간다.",
    "ISTP": "귀찮다고 보고 누락하고 혼자 몰래 땜질 처리하지 마라. 그 작은 땜질이 나중에 50억짜리 소송으로 터진다.",
    "INTP": "방구석에서 HS Code 법리 해석만 3주째 파고 있지 마라. 분석은 완벽한데 화물은 이미 세관에 압류당했다.",
    "INFJ": "바이어 눈빛 보고 혼자 섭섭해하며 속으로 손절각 재지 마라. 비즈니스는 연애가 아니라 돈 놓고 돈 먹기다.",
    "INFP": "클레임 메일 한 통 받고 멘탈 터져서 화장실에서 울지 마라. 바이어의 지랄은 네 인격 모독이 아니라 그냥 일상이다."
}

# 6대 무역 직무 데이터베이스[cite: 7, 8]
TRADE_JOBS = {
    "해외영업 (Global Sales)": {
        "badge": "GLOBAL FRONT-LINER",
        "tag": "🌐 전 세계 바이어의 지갑을 열어젖히는 수출 전선의 야전사령관",
        "trade_type_name": "글로벌 딜 메이커 & 시장 개척가",
        "image": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=1200&q=80",
        "duties": [
            "글로벌 신규 바이어 발굴 및 인콰이어리(Inquiry) 응대",
            "인코텀즈 2020 기반 수출 가격 협상 및 오퍼시트 발행",
            "해외 메이저 B2B 박람회 참가 및 대면 피칭 미팅 주도",
            "수출 대금 회수 일정 조율 및 고객 클레임 1차 방어"
        ],
        "competencies": [
            "글로벌 비즈니스 네고 감각",
            "거절에 굴하지 않는 회복탄력성",
            "타문화 공감 및 피칭 화술",
            "국제 무역 인코텀즈 2020 이해도"
        ],
        "synergy_tip": "꼼꼼한 서류 작업을 전담해 줄 '무역사무/물류관리' 포지션과 페어를 이룰 때 폭발적인 실적을 냅니다.",
        "match_types": ["ENTP", "ESTP", "ENTJ", "ESFJ"]
    },
    "무역사무 및 물류관리 (Trade Logistics & Ops)": {
        "badge": "SUPPLY-CHAIN TOWER",
        "tag": "📦 0.001%의 서류 오차도 찢어버리는 글로벌 공급망 관제탑",
        "trade_type_name": "공급망 무결점 수호자",
        "image": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1200&q=80",
        "duties": [
            "선하증권(B/L), 상업송장(C/I), 포장명세서(P/L) 등 선적 서류 정밀 작성 및 검수",
            "포워더(Forwarder) 및 선사 부킹, 컨테이너 스페이스 확보",
            "해상/항공 운송 추적 및 입항 지연(Demurrage) 리스크 모니터링",
            "적하보험 가입 및 운송 중 화물 파손/분실 사고 클레임 처리"
        ],
        "competencies": [
            "0.1% 오차도 잡아내는 서류 정밀성",
            "선박 스케줄링 및 위기관리 역량",
            "ERP 시스템 및 무역 서식 핸들링",
            "포워더 및 보세창고 협상력"
        ],
        "synergy_tip": "야전에서 바이어를 물어오는 '해외영업' 담당자의 든든한 백본이 되어 물류 딜레이를 완벽 방어합니다.",
        "match_types": ["ISTJ", "ESTJ", "ISFJ", "ISFP"]
    },
    "해외소싱 및 구매전략 (Global Sourcing & SCM)": {
        "badge": "STRATEGIC BUYER",
        "tag": "🔍 전 세계 숨겨진 가성비 공장과 원자재를 발굴하는 책략가",
        "trade_type_name": "원가 파괴 공급망 아키텍트",
        "image": "https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&w=1200&q=80",
        "duties": [
            "경쟁력 있는 해외 OEM/ODM 제조업체 및 원자재 공급사 발굴",
            "원가 명세서(Cost Breakdown) 세부 해체 분석 및 납품 단가 인하 협상",
            "현지 해외 공장 Q/C(품질관리) 실사 및 납기 준수 모니터링",
            "지정학적 리스크 대비 대체 공급망(Dual Sourcing) 구축"
        ],
        "competencies": [
            "데이터 기반 원가 분석력(Costing)",
            "공급업체 압박 및 윈윈 조율력",
            "글로벌 원자재 시세 모니터링 감각",
            "제조 공정 및 품질 규격 이해도"
        ],
        "synergy_tip": "'관세/통관전략' 팀과 긴밀히 협력해 FTA 무관세 혜택을 받는 원산지 공장을 발굴하면 원가를 극적으로 줄입니다.",
        "match_types": ["INTJ", "ISTP"]
    },
    "외환 및 무역금융 (Trade Finance & FX)": {
        "badge": "FX SHIELD ARCHITECT",
        "tag": "💳 요동치는 환율과 대금 미회수 리스크를 철벽 방어하는 자금 설계자",
        "trade_type_name": "외환 & 자금 방패 사령관",
        "image": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=1200&q=80",
        "duties": [
            "신용장(L/C) 조건 일치 여부 정밀 심사 및 은행 대금 네고(Nego)",
            "환율 변동 대비 선물환·통화선물 헤징(Hedging) 전략 수립",
            "수출입 신용보증기금 및 한국무역보험공사(K-SURE) 보험 청구",
            "바이어 결제 신용도 평가 및 D/A, D/P 결제 리스크 한도 설정"
        ],
        "competencies": [
            "외환 시장 트렌드 분석 및 리스크 헤징",
            "UCP600(신용장통일규칙) 법리 이해",
            "금융권 외환/여신 프로세스 이해",
            "수치 오차를 허용하지 않는 회계적 정밀함"
        ],
        "synergy_tip": "대규모 프로젝트 딜을 추진하는 '해외영업'과 공조하여 미수금 리스크 없는 안전한 결제조건을 설계합니다.",
        "match_types": ["ISTJ", "INTJ", "ESTJ"]
    },
    "관세 및 통관전략 (Customs & Compliance)": {
        "badge": "COMPLIANCE SPECIALIST",
        "tag": "⚖️ 촘촘한 관세법을 뚫고 합법적으로 세금을 증발시키는 법률 스페셜리스트",
        "trade_type_name": "무역 규제 & 절세 전략가",
        "image": "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=1200&q=80",
        "duties": [
            "수출입 품목에 대한 정확한 HS Code(품목분류) 10단위 판정",
            "국가 간 FTA 원산지 증명서(C/O) 발급 및 사후검증 대응",
            "관세 감면 및 환급(Drawback) 요건 검토를 통한 절세 실행",
            "수출입 요건 확인(식약처, KC인증, 전략물자 판정 등) 법적 리스크 사전 차단"
        ],
        "competencies": [
            "관세율표 및 통칙 해석 논리력",
            "FTA 원산지 판정 프로세스 지식",
            "국제 무역 규제 및 제재 법률 분석력",
            "정부 세관 대응 및 문서 설득력"
        ],
        "synergy_tip": "'해외소싱' 팀이 찾아온 신규 원자재의 관세율을 합법적으로 낮춰 회사의 마진율을 즉각 올려줍니다.",
        "match_types": ["INTP", "INFJ"]
    },
    "글로벌 마케팅 (Global Trade Marketing)": {
        "badge": "CREATIVE TRENDSETTER",
        "tag": "🎨 글로벌 트렌드를 선점해 전 세계에 판을 까는 크리에이터",
        "trade_type_name": "국경 없는 트렌드 기획자",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80",
        "duties": [
            "해외 권역별 타깃 바이어 페르소나 정의 및 온/오프라인 캠페인 기획",
            "글로벌 엑스포 독립 부스 인테리어 기획 및 현장 바이럴 이벤트 총괄",
            "아마존 글로벌셀링, 알리바바, 쇼피 등 B2B/B2C 플랫폼 입점 및 광고 운영",
            "현지 문화와 트렌드를 반영한 제품 패키징 및 카탈로그 현지화"
        ],
        "competencies": [
            "글로벌 소비자/바이어 심리 인사이트",
            "해외 전시회 부스 공간 기획력",
            "디지털 글로벌 그로스 마케팅 스킬",
            "언어와 문화를 뛰어넘는 시각적 스토리텔링"
        ],
        "synergy_tip": "'해외영업' 팀이 바이어와 미팅할 수 있도록 양질의 바이어 리드(Inbound Lead)를 대량으로 유입시킵니다.",
        "match_types": ["ENFJ", "ENFP", "ESFP", "INFP"]
    }
}

# 실제 MBTI 대응 직무 매핑[cite: 7, 8]
MBTI_MAP = {
    "ENTP": "해외영업 (Global Sales)",
    "ESTP": "해외영업 (Global Sales)",
    "ENTJ": "해외영업 (Global Sales)",
    "ESFJ": "해외영업 (Global Sales)",
    "ISTJ": "무역사무 및 물류관리 (Trade Logistics & Ops)",
    "ESTJ": "무역사무 및 물류관리 (Trade Logistics & Ops)",
    "ISFJ": "무역사무 및 물류관리 (Trade Logistics & Ops)",
    "ISFP": "무역사무 및 물류관리 (Trade Logistics & Ops)",
    "INTJ": "해외소싱 및 구매전략 (Global Sourcing & SCM)",
    "ISTP": "해외소싱 및 구매전략 (Global Sourcing & SCM)",
    "INTP": "관세 및 통관전략 (Customs & Compliance)",
    "INFJ": "관세 및 통관전략 (Customs & Compliance)",
    "ENFP": "글로벌 마케팅 (Global Trade Marketing)",
    "ENFJ": "글로벌 마케팅 (Global Trade Marketing)",
    "ESFP": "글로벌 마케팅 (Global Trade Marketing)",
    "INFP": "글로벌 마케팅 (Global Trade Marketing)"
}

# 세션 상태 초기화[cite: 7, 8]
if "stage" not in st.session_state:
    st.session_state.stage = "INTRO"
if "answers" not in st.session_state:
    st.session_state.answers = {}

# ==========================================
# 1. 인트로 화면 (화면 정중앙 배치)[cite: 7, 8]
# ==========================================
if st.session_state.stage == "INTRO":
    col_out_left, col_center, col_out_right = st.columns([1, 2.5, 1])
    with col_center:
        st.markdown("""
        <div class='intro-box'>
            <div class='intro-badge'>GLOBAL TRADE APTITUDE TEST</div>
            <div class='intro-title'>✨ 글로벌 무역 T-MBTI 파인더</div>
            <div class='intro-desc'>
                바이어와의 야간 샷 배틀부터 컨테이너 셧다운, 환율 폭락, 30억 부도 위기까지!<br>
                숨 막히는 <b>20가지 실전 무역 비즈니스 극단 난제 시나리오</b> 속에서<br>
                나의 <b>실제 MBTI</b>와 무역 전용 <b>T-MBTI</b>, 그리고 <b>6대 무역직무</b>를 발견하세요.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col_b1, col_b2, col_b3 = st.columns([1, 1.8, 1])
        with col_b2:
            if st.button("🚀 무역 MBTI 검사 시작하기", use_container_width=True, type="primary"):
                st.session_state.stage = "STEP_1"
                st.rerun()

# ==========================================
# 2. 질문 단계 화면 (🔥 화면 정중앙 배치 & 버튼 가운데 정렬)[cite: 7, 8]
# ==========================================
elif st.session_state.stage in ["STEP_1", "STEP_2", "STEP_3", "STEP_4", "STEP_5"]:
    step_map = {
        "STEP_1": (1, 0, 4),   # Q1 ~ Q4[cite: 7, 8]
        "STEP_2": (2, 4, 8),   # Q5 ~ Q8[cite: 7, 8]
        "STEP_3": (3, 8, 12),  # Q9 ~ Q12[cite: 7, 8]
        "STEP_4": (4, 12, 16), # Q13 ~ Q16[cite: 7, 8]
        "STEP_5": (5, 16, 20)  # Q17 ~ Q20[cite: 7, 8]
    }
    step_num, start_idx, end_idx = step_map[st.session_state.stage]
    current_questions = QUESTIONS[start_idx:end_idx]

    # 좌우 여백을 주어 중앙에 깔끔하게 모이도록 3열 그리드 적용
    col_margin_left, col_main, col_margin_right = st.columns([1, 2.6, 1])

    with col_main:
        st.markdown(f"<div style='text-align: center; margin-bottom: 0.5rem;'><h3 style='display:inline-block; color:#1E293B;'>🧭 SCENARIO PROGRESS : STEP {step_num} / 5</h3></div>", unsafe_allow_html=True)
        st.progress(step_num / 5)
        st.write("")

        current_step_choices = {}
        for item in current_questions:
            st.markdown(f"""
            <div class='q-card'>
                <div class='q-header-row'>
                    <div class='q-icon-avatar'>{item['icon']}</div>
                    <div>
                        <span class='q-badge'>SCENARIO #{item['id']:02d}</span>
                        <span class='q-tag-text'>&nbsp;• {item['tag']}</span>
                    </div>
                </div>
                <div class='q-title'>{item['q']}</div>
            </div>
            """, unsafe_allow_html=True)

            opt1 = item["options"][0][1]
            opt2 = item["options"][1][1]

            prev_val = None
            if item['id'] in st.session_state.answers:
                prev_code = st.session_state.answers[item['id']]
                prev_val = opt1 if prev_code == item["options"][0][0] else opt2

            selected = st.radio(
                label=f"Q{item['id']}",
                options=[opt1, opt2],
                index=[opt1, opt2].index(prev_val) if prev_val else None,
                key=f"radio_{item['id']}",
                label_visibility="collapsed"
            )
            current_step_choices[item['id']] = selected

        st.write("")
        
        # 🔥 다음/이전 버튼 영역: 가운데 정렬
        btn_center_left, btn_center_mid, btn_center_right = st.columns([1, 2, 1])
        
        with btn_center_mid:
            if step_num > 1:
                col_btn_prev, col_btn_next = st.columns([1, 1])
                with col_btn_prev:
                    if st.button("⬅️ 이전으로", use_container_width=True):
                        for q_id, sel in current_step_choices.items():
                            if sel:
                                opt_a = QUESTIONS[q_id-1]["options"][0]
                                code = opt_a[0] if sel == opt_a[1] else QUESTIONS[q_id-1]["options"][1][0]
                                st.session_state.answers[q_id] = code
                        st.session_state.stage = f"STEP_{step_num - 1}"
                        st.rerun()
                with col_btn_next:
                    btn_label = "다음으로 ➡️" if step_num < 5 else "🔥 최종 결과 확인"
                    if st.button(btn_label, use_container_width=True, type="primary"):
                        unanswered = [q_id for q_id, val in current_step_choices.items() if val is None]
                        if unanswered:
                            st.error(f"⚠️ 4개 시나리오를 모두 체크해야 합니다. (미선택: Q{', Q'.join(map(str, unanswered))})")
                        else:
                            for q_id, sel in current_step_choices.items():
                                opt_a = QUESTIONS[q_id-1]["options"][0]
                                code = opt_a[0] if sel == opt_a[1] else QUESTIONS[q_id-1]["options"][1][0]
                                st.session_state.answers[q_id] = code

                            if step_num < 5:
                                st.session_state.stage = f"STEP_{step_num + 1}"
                            else:
                                st.session_state.stage = "RESULT"
                            st.rerun()
            else:
                # 1단계일 때는 '다음으로' 버튼만 단독으로 가운데 풀사이즈 배치
                if st.button("다음으로 ➡️", use_container_width=True, type="primary"):
                    unanswered = [q_id for q_id, val in current_step_choices.items() if val is None]
                    if unanswered:
                        st.error(f"⚠️ 4개 시나리오를 모두 체크해야 합니다. (미선택: Q{', Q'.join(map(str, unanswered))})")
                    else:
                        for q_id, sel in current_step_choices.items():
                            opt_a = QUESTIONS[q_id-1]["options"][0]
                            code = opt_a[0] if sel == opt_a[1] else QUESTIONS[q_id-1]["options"][1][0]
                            st.session_state.answers[q_id] = code
                        st.session_state.stage = "STEP_2"
                        st.rerun()

# ==========================================
# 3. 최종 결과 화면 (RESULT DASHBOARD)[cite: 7, 8]
# ==========================================
elif st.session_state.stage == "RESULT":
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    for _, code in st.session_state.answers.items():
        scores[code] += 1

    real_mbti = ""
    real_mbti += "E" if scores["E"] >= scores["I"] else "I"
    real_mbti += "S" if scores["S"] >= scores["N"] else "N"
    real_mbti += "T" if scores["T"] >= scores["F"] else "F"
    real_mbti += "J" if scores["J"] >= scores["P"] else "P"

    trade_mbti = ""
    trade_mbti += TRADE_AXIS[real_mbti[0]][0]
    trade_mbti += TRADE_AXIS[real_mbti[1]][0]
    trade_mbti += TRADE_AXIS[real_mbti[2]][0]
    trade_mbti += TRADE_AXIS[real_mbti[3]][0]

    matched_job_name = MBTI_MAP.get(real_mbti, "해외영업 (Global Sales)")
    job = TRADE_JOBS[matched_job_name]
    fault_comment = MBTI_FAULT_FIX.get(real_mbti, "기본에 충실하라.")

    st.balloons()

    # 상단 배너 + 초대형 단점 경고 전광판[cite: 7, 8]
    st.markdown(f"""
    <div class='dash-hero'>
        <div style='display: inline-block; background: #3B82F6; color: white; font-size: 0.85rem; font-weight: 800; padding: 0.35rem 1rem; border-radius: 9999px; margin-bottom: 0.8rem; letter-spacing: 0.05em;'>
            {job['badge']}
        </div>
        <div class='type-compare-container'>
            <!-- 무역 전용 T-MBTI 박스 -->
            <div class='type-pill'>
                <div class='type-pill-title'>🌐 무역 전용 T-MBTI</div>
                <div class='type-pill-val-trade'>{trade_mbti}</div>
                <div style='color: #FCA5A5; font-size: 1.05rem; font-weight: 800; margin-top: 4px;'>{job['trade_type_name']}</div>
                <div style='color: #94A3B8; font-size: 0.82rem; margin-top: 6px;'>무역 실무 행동 패턴으로 도출된 전용 코드</div>
            </div>
            <!-- 실제 일상 MBTI 박스 -->
            <div class='type-pill'>
                <div class='type-pill-title'>🧠 상응하는 실제 MBTI</div>
                <div class='type-pill-val-real'>{real_mbti}</div>
                <div style='color: #93C5FD; font-size: 1.05rem; font-weight: 800; margin-top: 4px;'>성향 싱크로율 100% 매칭</div>
                <div style='color: #94A3B8; font-size: 0.82rem; margin-top: 6px;'>일상 속 의사결정 행동 패턴 분석 결과</div>
            </div>
        </div>
        <div style='font-size: 2.3rem; font-weight: 800; color: #F8FAFC; margin-top: 0.5rem;'>{matched_job_name}</div>
        <div style='font-size: 1.15rem; color: #CBD5E1;'>{job['tag']}</div>
    </div>

    <!-- 초대형 단점 경고 전광판 배너 -->
    <div class='fault-fix-mega-box'>
        <div class='fault-fix-badge'>🚨 {real_mbti} 무역 실무 치명적 단점 긴급 경고</div>
        <div class='fault-fix-mega-text'>"{fault_comment}"</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # 2열 구성 패널[cite: 7, 8]
    col_left, col_right = st.columns([1.1, 1])

    with col_left:
        st.image(job["image"], use_container_width=True, caption=f"⚡ 추천 무역 포지션: {matched_job_name}")

    with col_right:
        st.markdown("""
        <div class='dash-panel'>
            <h3>📊 무역 T-MBTI 스펙트럼 분석</h3>
            <div style='color: #64748B; font-size: 0.88rem; margin-bottom: 1rem;'>실제 MBTI 지표를 무역 비즈니스 관점의 4대 핵심 축으로 환산한 지표입니다.</div>
        """, unsafe_allow_html=True)

        st.write(f"⚡ **[F] 개척(E)** {scores['E']*20}% vs **[B] 수호(I)** {scores['I']*20}%")
        st.progress(scores['E'] / 5)

        st.write(f"👁️ **[D] 정밀(S)** {scores['S']*20}% vs **[V] 비전(N)** {scores['N']*20}%")
        st.progress(scores['S'] / 5)

        st.write(f"🧠 **[N] 협상(T)** {scores['T']*20}% vs **[R] 관계(F)** {scores['F']*20}%")
        st.progress(scores['T'] / 5)

        st.write(f"🎯 **[S] 통제(J)** {scores['J']*20}% vs **[A] 기동(P)** {scores['P']*20}%")
        st.progress(scores['J'] / 5)

        st.markdown("""
        <div style='background: #F8FAFC; border: 1px solid #E2E8F0; padding: 0.85rem; border-radius: 8px; margin-top: 1rem; font-size: 0.86rem; color: #475569;'>
            💡 <b>T-MBTI 4대 축 가이드</b><br>
            • <b>F/B</b> : Frontier(시장개척) vs Backbone(내부수호)<br>
            • <b>D/V</b> : Detail(수치정밀) vs Vision(전략기획)<br>
            • <b>N/R</b> : Nego(냉철협상) vs Relation(신뢰관계)<br>
            • <b>S/A</b> : System(원칙통제) vs Agile(유연기동)
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # R&R 및 핵심 역량 대시보드[cite: 7, 8]
    col_rr, col_skill = st.columns(2)

    with col_rr:
        st.markdown("""
        <div class='dash-panel'>
            <h3>📋 이 직무가 하는 일 (Core R&R)</h3>
            <div style='color: #64748B; font-size: 0.9rem; margin-bottom: 1rem;'>실제 종합상사 및 제조사 무역부서의 실무 프로세스입니다.</div>
        """, unsafe_allow_html=True)
        for duty in job["duties"]:
            st.markdown(f"<div class='rr-item'>{duty}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_skill:
        st.markdown("""
        <div class='dash-panel'>
            <h3>🚀 갖추어야 할 핵심 역량 (Key Competencies)</h3>
            <div style='color: #64748B; font-size: 0.9rem; margin-bottom: 1rem;'>무역 실무 및 취업 면접에서 강력한 무기가 되는 스킬셋입니다.</div>
        """, unsafe_allow_html=True)
        skills_html = "".join([f"<span class='skill-chip'>✓ {s}</span>" for s in job["competencies"]])
        st.markdown(f"<div>{skills_html}</div>", unsafe_allow_html=True)

        st.markdown("<h4 style='color: #0F172A; margin-top: 1.5rem; font-size: 1.05rem;'>🤝 조직 내 비즈니스 시너지</h4>", unsafe_allow_html=True)
        st.markdown(f"<div style='color: #475569; font-size: 0.95rem; line-height: 1.6;'>{job['synergy_tip']}</div>", unsafe_allow_html=True)

        st.markdown("<h4 style='color: #0F172A; margin-top: 1.2rem; font-size: 1.05rem;'>👥 적합 일상 MBTI 유형</h4>", unsafe_allow_html=True)
        mbti_badges = " ".join([f"<b style='color:#4F46E5; background: #EEF2FF; border: 1px solid #C7D2FE; padding: 3px 8px; border-radius: 6px;'>{m}</b>" for m in job["match_types"]])
        st.markdown(mbti_badges, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    col_r1, col_r2, col_r3 = st.columns([1, 1, 1])
    with col_r2:
        if st.button("🔄 검사 다시 시작하기", use_container_width=True):
            st.session_state.stage = "INTRO"
            st.session_state.answers = {}
            st.rerun()