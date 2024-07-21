"""
화면에 챗봇 만들어 보기 - OpenAI로 직접(랭체인 x)
단점 : 대화 흐름을 기억못함. 
"""

from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

# 환경변수 업로드 (api 키)
load_dotenv()

st.title("간단한 챗봇 만들기")
input = st.text_input("질문을 해보세요", "")

if len(input) > 0:
    st.write(f"입력: {input}")
    
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "당신은 친절한 여행 전문가입니다.",
            },
            {
                "role": "user",
                "content": input,
            },
        ],
        max_tokens=2048,
    )
    st.write(response.choices[0].message.content)
    print(response.choices[0].message)
    print(response.model)
