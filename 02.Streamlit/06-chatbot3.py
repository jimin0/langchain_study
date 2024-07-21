"""
화면에 챗봇 만들어 보기 - LangChain 사용 (OpenAI) -> 역할 x, 답변도 객체반환이 아닌 문자열로 바로 반환
단점 : 여전히 대화 흐름을 기억못함. 답변 형식적이고 짧음. 
"""
from langchain_openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# Streamlit 앱 제목 설정
st.title("간단한 챗봇 만들기")
input = st.text_input("질문을 해보세요", "")

if len(input) > 0:
    st.write(f"입력: {input}")

    llm = OpenAI()
    
    # LangChain을 사용하여 챗봇 응답 생성
    response = llm.invoke(input)
    
    # 생성된 응답 표시
    st.write(response)