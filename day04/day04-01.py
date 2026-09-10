import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -------------------------------------------------------------------
# 1. 기본 설정 및 데이터 로드
# -------------------------------------------------------------------
st.set_page_config(page_title="무역 데이터 분석 대시보드", layout="wide")

@st.cache_data
def load_data(path):
    # CSV 파일 읽기
    df = pd.read_csv(path)
    
    # '날짜' 컬럼이 존재할 경우 datetime 타입으로 변환 (선택 사항)
    if '날짜' in df.columns:
        df['날짜'] = pd.to_datetime(df['날짜'])
        
    return df

def main():
    st.title("📊 무역 데이터 분석 대시보드 (조건 필터링)")
    st.markdown("특정 조건(HS코드 85, 미국/베트남, 수출금액 0 초과)으로 필터링하고 상위 10건을 도출합니다.")

    # 1. 파일 경로 설정 (상대 경로 방식)
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'common', 'raw_trade_data.csv')

    try:
        # 데이터 로드 (이제 file_path 변수를 올바르게 전달합니다)
        df = load_data(file_path)

        # -------------------------------------------------------------------
        # 2. 필수 요구사항 (다중 조건 필터링)
        # -------------------------------------------------------------------
        # HS코드를 문자열로 변환하여 앞 두 자리가 '85'인지 확인
        if 'HS코드' in df.columns:
            cond_hs = df['HS코드'].astype(str).str.startswith('85')
        elif '품목코드' in df.columns:
            cond_hs = df['품목코드'].astype(str).str.startswith('85')
        else:
            # 컬럼 이름이 다를 경우 무조건 참 처리 (오류 방지)
            cond_hs = True

        cond_country = df['국가명'].isin(['미국', '베트남'])
        cond_amount = df['수출금액'] > 0

        # 위 세 가지 조건을 모두 만족하는 데이터 필터링
        filtered_req_df = df[cond_hs & cond_country & cond_amount]

        # 수출금액 기준 내림차순 정렬 후 상위 10건 추출
        top_10_df = filtered_req_df.sort_values(by='수출금액', ascending=False).head(10)

        # -------------------------------------------------------------------
        # 3. 화면 출력 및 파일 저장 (report.csv)
        # -------------------------------------------------------------------
        st.subheader("💡 다중 조건 필터링 결과 (상위 10건)")
        st.markdown("* **조건:** HS코드 85 시작 & 국가명(미국/베트남) & 수출금액 > 0")
        
        if not top_10_df.empty:
            st.dataframe(top_10_df, use_container_width=True)
            
            # report.csv 파일로 저장 (현재 실행되는 폴더에 저장)
            save_path = os.path.join(current_dir, 'report.csv')
            top_10_df.to_csv(save_path, index=False, encoding='utf-8-sig')
            st.success(f"✅ 상위 10건 데이터가 `{save_path}`에 성공적으로 저장되었습니다!")
        else:
            st.warning("해당 조건을 만족하는 데이터가 존재하지 않습니다.")

        st.divider()

        # -------------------------------------------------------------------
        # 4. 일반 대시보드 기능 (사이드바 및 전체 현황)
        # -------------------------------------------------------------------
        st.sidebar.header("🔍 전체 데이터 필터 설정")
        
        # 일반 대시보드용 필터
        countries = st.sidebar.multiselect("국가 선택", options=df['국가명'].unique(), default=df['국가명'].unique())
        
        if '품목명' in df.columns:
            items = st.sidebar.multiselect("품목 선택", options=df['품목명'].unique(), default=df['품목명'].unique())
            dashboard_df = df[(df['국가명'].isin(countries)) & (df['품목명'].isin(items))]
        else:
            dashboard_df = df[df['국가명'].isin(countries)]

        st.subheader("📊 필터링된 전체 데이터 현황")
        
        # 주요 지표 (KPI)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("총 수출금액", f"{dashboard_df['수출금액'].sum():,.0f}")
        with col2:
            weight = dashboard_df['중량'].sum() if '중량' in dashboard_df.columns else 0
            st.metric("총 중량", f"{weight:,.2f}")
        with col3:
            st.metric("데이터 행 수", f"{len(dashboard_df):,} 건")

        # 시각화
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.markdown(" **국가별 수출금액 비중**")
            if not dashboard_df.empty:
                country_sum = dashboard_df.groupby('국가명')['수출금액'].sum().reset_index()
                fig_pie = px.pie(country_sum, values='수출금액', names='국가명', hole=0.4)
                st.plotly_chart(fig_pie, use_container_width=True)

        with chart_col2:
             st.markdown(" **국가별 총 수출금액 (Bar)**")
             if not dashboard_df.empty:
                fig_bar = px.bar(country_sum, x='국가명', y='수출금액', color='국가명')
                st.plotly_chart(fig_bar, use_container_width=True)

    except FileNotFoundError:
        st.error(f"❌ 파일을 찾을 수 없습니다: {file_path}\n\n경로 설정(`../common/raw_trade_data.csv`)을 다시 확인해 주세요.")
    except Exception as e:
        st.error(f"❌ 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()