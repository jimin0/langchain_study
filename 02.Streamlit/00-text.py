import streamlit as st

# 타이틀 적용
st.title("Langchain과 LLM을 활용한 application 개발 :100:")

# 특수 이모티콘 삽입 예시
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# caption은 설명을 추가할 때 사용

st.caption(
    """
    랭체인 공부 3일차, 조금씩 발전 중이에요 :smile:
    스트림릿 프로그램 만들기~~ :computer:와 함께
    파이팅입니다. 나자신 :rocket:
           """
)

# Header 적용
st.header("1. API key setting :sparkles:")

# Subheader 적용
st.subheader("1.1. OpenAI API key setting")


# 코드 표시
sample_code = """
# OpenAI API 테스트

from openai import OpenAI
client = OpenAI()
try:
    client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {
            "role": "system",
            "content": "당신은 친절한 AI Assistance 입니다.",
        },
        {
            "role": "user",
            "content": "say this is test",
        },
        ],
        max_tokens=2024
    )
    print("OpenAI API 성공")
except Exception:
    print("OpenAI API 실패")
"""
st.code(sample_code, language="python")

# 일반 텍스트
st.text(
    """
API 키 보안: API 키는 민감한 정보이므로 코드에 하드코딩하지 말고 환경 변수나 비밀 관리 시스템을 사용하여 관리하세요.
요금제 확인: API 사용량에 따라 비용이 발생할 수 있으므로, OpenAI 계정의 요금제와 사용량을 정기적으로 확인하세요..
"""
)

# 마크다운 문법 지원
st.markdown(
    """
# 헤드라인1 (마크다운 문법) 
## 헤드라인2
### 헤드라인3
- bullet1
- bullet2
- bullet3
    - bullet3-1
        - bullet3-2

    """
)


# 컬러코드: blue, green, orange, red, violet
st.subheader("글자 색상 지정하기")
st.markdown(
    "텍스트의 색상을 :red[빨간색]으로, 그리고 **:blue[파란색]** 볼드체로 설정할 수 있습니다."
)


st.subheader("수식(라텍스) 표현하기")
st.markdown(
    ":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다 :pencil:"
)
