import streamlit as st
import random
#안녕~
# 페이지 기본 설정
st.set_page_config(
    page_title="신나는 구구단 교실",
    page_icon="🔢",
    layout="wide"
)

# 제목 및 소개
st.title("🔢 신나는 구구단 교실 🎒")
st.caption("Streamlit으로 만든 양방향 구구단 학습 및 퀴즈 프로그램입니다.")

st.markdown("---")

# 탭 구성: 구구단 학습 / 구구단 퀴즈
tab1, tab2 = st.tabs(["📖 구구단 학습하기", "🧠 구구단 퀴즈 풀기"])

# ==================== TAB 1: 구구단 학습하기 ====================
with tab1:
    st.header("📖 구구단 공부방")
    st.write("원하는 단을 선택해서 공부하거나, 전체 구구단을 한눈에 확인해보세요.")
    
    # 학습 모드 선택
    study_mode = st.radio(
        "학습 모드를 선택하세요",
        ["특정 단만 보기", "전체 구구단 한눈에 보기"],
        horizontal=True
    )
    
    if study_mode == "특정 단만 보기":
        # Slider로 단 선택하기 (2단 ~ 9단)
        dan = st.slider("확인하고 싶은 단을 선택하세요", min_value=2, max_value=9, value=2, step=1)
        
        st.subheader(f"🎯 {dan}단 공부하기")
        
        # 3열 레이아웃으로 구구단을 예쁘게 배치
        cols = st.columns(3)
        for i in range(1, 10):
            with cols[(i-1) % 3]:
                st.info(f"**{dan}** × **{i}** = **{dan * i}**")
                
    else:
        st.subheader("📊 전체 구구단 표 (2단 ~ 9단)")
        
        # 4열 레이아웃 구성 (2~5단 첫 줄, 6~9단 둘째 줄)
        st.markdown("### 🔹 2단 ~ 5단")
        cols_first_row = st.columns(4)
        for d in range(2, 6):
            with cols_first_row[d-2]:
                st.markdown(f"#### 📍 {d}단")
                for i in range(1, 10):
                    st.write(f"{d} × {i} = **{d * i}**")
        
        st.markdown("---")
        
        st.markdown("### 🔹 6단 ~ 9단")
        cols_second_row = st.columns(4)
        for d in range(6, 10):
            with cols_second_row[d-6]:
                st.markdown(f"#### 📍 {d}단")
                for i in range(1, 10):
                    st.write(f"{d} × {i} = **{d * i}**")

# ==================== TAB 2: 구구단 퀴즈 풀기 ====================
with tab2:
    st.header("🧠 구구단 실력 테스트")
    st.write("무작위로 나오는 구구단 문제를 맞혀보세요!")

    # 세션 상태 초기화
    if "quiz_num1" not in st.session_state:
        st.session_state.quiz_num1 = random.randint(2, 9)
        st.session_state.quiz_num2 = random.randint(1, 9)
        st.session_state.score = 0
        st.session_state.total_questions = 0
        st.session_state.quiz_answered = False
        st.session_state.last_feedback = ""
        st.session_state.last_is_correct = False

    num1 = st.session_state.quiz_num1
    num2 = st.session_state.quiz_num2

    # 퀴즈 레이아웃
    col_q, col_score = st.columns([2, 1])

    with col_q:
        st.markdown(f"### **Q. {num1} × {num2} = ?**")
        
        # 입력 폼
        with st.form(key="quiz_form", clear_on_submit=True):
            user_ans = st.number_input("정답을 입력하세요:", min_value=0, max_value=100, step=1, format="%d", value=None, placeholder="여기에 정답 입력...")
            submit_button = st.form_submit_button(label="정답 제출")

        if submit_button:
            if user_ans is None:
                st.warning("정답을 입력한 후 제출해 주세요!")
            elif st.session_state.quiz_answered:
                st.info("이미 문제를 풀었습니다. '다음 문제' 버튼을 눌러 다음으로 넘어가세요.")
            else:
                correct_ans = num1 * num2
                st.session_state.total_questions += 1
                st.session_state.quiz_answered = True
                
                if user_ans == correct_ans:
                    st.session_state.score += 1
                    st.session_state.last_feedback = f"🎉 정답입니다! {num1} × {num2} = {correct_ans}"
                    st.session_state.last_is_correct = True
                else:
                    st.session_state.last_feedback = f"❌ 아쉽습니다! 오답입니다. 정답은 {correct_ans} 입니다."
                    st.session_state.last_is_correct = False

        # 제출 후 결과 메시지 표시
        if st.session_state.quiz_answered:
            if st.session_state.last_is_correct:
                st.success(st.session_state.last_feedback)
            else:
                st.error(st.session_state.last_feedback)

            # 다음 문제 풀기 버튼
            if st.button("다음 문제 ➡️"):
                st.session_state.quiz_num1 = random.randint(2, 9)
                st.session_state.quiz_num2 = random.randint(1, 9)
                st.session_state.quiz_answered = False
                st.session_state.last_feedback = ""
                st.rerun()

    with col_score:
        st.markdown("### 🏆 내 점수")
        st.metric(label="맞힌 문제 수 / 전체 문제 수", value=f"{st.session_state.score} / {st.session_state.total_questions}")
        
        # 정답률 계산
        if st.session_state.total_questions > 0:
            accuracy = (st.session_state.score / st.session_state.total_questions) * 100
            st.write(f"현재 정답률: **{accuracy:.1f}%**")
            st.progress(accuracy / 100.0)
        
        # 점수 초기화 버튼
        if st.button("점수 초기화 🔄"):
            st.session_state.quiz_num1 = random.randint(2, 9)
            st.session_state.quiz_num2 = random.randint(1, 9)
            st.session_state.score = 0
            st.session_state.total_questions = 0
            st.session_state.quiz_answered = False
            st.session_state.last_feedback = ""
            st.rerun()
