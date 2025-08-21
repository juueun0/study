from streamlit_gsheets import GSheetsConnection
import streamlit as st
import pandas as pd

# 1. 구글시트 URL 불러오기 (streamlit secrets에서 관리)
url = st.secrets["gsheets"]["url"]

# 2. 연결
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url)

# 3. 학번·이름 입력 후 필터링
학번 = st.text_input("학번 입력")
이름 = st.text_input("이름 입력")

if st.button("조회"):
    result = df[(df["학번"] == 학번) & (df["이름"] == 이름)]
    if not result.empty:
        st.dataframe(result)
    else:
        st.warning("해당하는 정보가 없습니다.")
