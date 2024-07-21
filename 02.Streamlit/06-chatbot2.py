"""
화면에 챗봇 만들어 보기 - LangChain 사용 (import ChatOpenAI)
단점 : 여전히 대화 흐름을 기억못함.
하지만 확장성은 있는 듯?
"""

from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Streamlit 앱 제목 설정
st.title("간단한 챗봇 만들기 2 : langchain 사용")
input = st.text_input("질문을 해보세요", "")

if len(input) > 0:
    st.write(f"입력: {input}")

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    # 메세지 리스트 생성 : 시스템 메시지와 사용자 입력 포함.
    messages = [
        {"role": "system", "content": "당신은 친절한 여행 전문가입니다."},
        {"role": "user", "content": input},
    ]

    # LangChain을 사용하여 챗봇 응답 생성  : invoke() 메서드 사용
    response = llm.invoke(messages).content

    # 생성된 응답 표시
    st.write(response)
