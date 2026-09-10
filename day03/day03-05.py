# 인코딩 자동 감지 + 한글 폰트 막대그래프
# 여러 인코딩('ftf-8-sig', 'cp949','euc-kr') 순서대로 시도
# 내가 쓸 폰트 같은 경로에 있어야 함
# 막대 그래프 생성 후 그림으로 저장    chart.png
# 실행  streamlit run day03-05.py


# CSV_PATH = os.path.join(os.path.dirname(__file__),'..','common','raw_trade_data.csv')
# CSV_PATH = '..\common\Titanic.csv'

import os
import matplotlib.pyplot as plt

import pandas as pd
import streamlit as st
from matplotlib import font_manager

st.title('인코딩 자동 감지 + 한글 폰트 막대그래프(titanic 연습)')
st.caption('여러 인코딩을 순서대로 시도해서 파일을 읽고, 객실등급별 생존율을 그래프로 그립니다.')

CSV_PATH = os.path.join(os.path.dirname(__file__), 'titanic_cleaned.csv')
FONT_PATH = os.path.join(os.path.dirname(__file__),'day03/BebasNeue-Regular.ttf')

from typing import List, Optional
import pandas as pd


def read_csv_with_auto_encoding(
    filepath_or_buffer, encodings: Optional[List[str]] = None, **kwargs
) -> Optional[pd.DataFrame]:
  """여러 인코딩 방식을 순서대로 시도하여 CSV 파일을 DataFrame으로 불러옵니다.

  ftf-8-sig(오타)는 자동으로 utf-8-sig로 보정되어 처리됩니다.
  """
  if encodings is None:
    # 기본 시도 목록 (오타 보정 포함)
    encodings = ['utf-8-sig', 'utf-8', 'cp949', 'euc-kr', 'latin1']

  # 'ftf-8-sig' 같은 흔한 오타를 'utf-8-sig'로 치환
  normalized_encodings = [
      'utf-8-sig' if enc == 'ftf-8-sig' else enc for enc in encodings
  ]

  for enc in normalized_encodings:
    try:
      # st.file_uploader로 전달받은 메모리 버퍼인 경우 파일 포인터를 처음으로 되돌림
      if hasattr(filepath_or_buffer, 'seek'):
        filepath_or_buffer.seek(0)

      df = pd.read_csv(filepath_or_buffer, encoding=enc, **kwargs)
      return df
    except (UnicodeDecodeError, LookupError):
      continue

  return None


#인코딩 자동 감지로 csv읽기
st.subheader('1) 인코딩 자동 감지')
df = read_csv_with_auto_encoding(CSV_PATH)

st.markdown('---')
# 객실등급(pclass) 별 생존율 집계
# 사망0 / 생존 1 등급별 평균을 내면 
# 그대로가 등급의 생존 비율이 된다.
# 10명 남 3 여자 7
# 1000 생존 300 300/1000 30% 

pclass_survival_rate = df.groupby('Pclass')['Survived'].mean().sort_index()
st.dataframe((pclass_survival_rate * 100).round(1).rename('생존율(%)'))

survival_df = (pclass_survival_rate * 100).round(1).rename('생존율(%)')
st.dataframe(survival_df)

# 차트 그리기
st.markdown('---')
st.subheader('3) 객실등급별 생존율 막대그래프')
try : 
    # 폰트 파일이 없으면 FileNotFoundError가 발생
    font_prop = font_manager.FontProperties(fname=FONT_PATH)
    # matplotlib font_manager에 폰트를 등록하고, 전역 폰트로 설정 
    font_manager.fontManager.addfont(FONT_PATH)
    plt.rcParams['font.family']=font_prop.get_name()
except FileNotFoundError:
    st.warning('폰트파일을 찾을 수가 없습니다.')

fig, ax = plt.subplots(figsize=(8,5))
(pclass_survival_rate *100).plot(kind='bar',color='blue',ax=ax)
ax.set_title('객실 등급별 생존율')
ax.set_xlabel('객실등급(Pclass)')
ax.set_ylabel('생존율(%)')

st.pyplot(fig)

output_png = os.path.join(os.path.dirname(__file__), 'chart.png')
fig.savefig(output_png)

