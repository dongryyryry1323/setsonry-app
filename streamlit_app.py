import streamlit as st
from openai import OpenAI

st.title("감각통합 소견서 생성기")

name = st.text_input("이름")
age = st.text_input("나이")
diagnosis = st.text_input("진단명")
test = st.text_input("검사도구")
result = st.text_input("검사결과")

sensory = st.text_area("감각특성")
motor = st.text_area("운동특성")
fine = st.text_area("미세운동")
language = st.text_area("언어")
behavior = st.text_area("행동특성")

if st.button("소견서 생성"):

    prompt = f"""
다음 정보를 바탕으로 감각통합치료 소견서를 작성하시오.

구성:
1. 현재 상태
2. 치료 방향 (5개)
3. 소견

이름: {name}
나이: {age}
진단명: {diagnosis}
검사도구: {test}
검사결과: {result}

감각특성: {sensory}
운동특성: {motor}
미세운동: {fine}
언어: {language}
행동특성: {behavior}
"""

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    st.write(response.output_text)
