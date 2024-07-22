import streamlit as st
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_teddynote.prompts import load_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages.chat import ChatMessage

# 앱 제목 및 설명 설정
st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

# 세션 상태 초기화
if "sessions" not in st.session_state:
    st.session_state.sessions = []


# 사이드바에 OpenAI API 키 입력 필드 생성  :
with st.sidebar:
    clear_btn = st.button("Clear Chat")
    openai_api_key = st.text_input(
        "OpenAI API Key", key="chatbot_api_key", type="password"
    )
    selected_prompt = st.selectbox(
        "프롬프트를 선택해 주세요",
        ("기본모드", "인스타", "트위터", "네이버 블로그", "기술 블로그"),
        index=0,
    )
    st.markdown("---")
    st.subheader("대화 세션 관리")


# 이전 대화를 출력
def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)


def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))


def create_chain(prompt_type):
    # prompt | llm | output_parser
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "당신은 친절한 AI 어시스턴트입니다. 다음의 질문에 간결하게 답변해 주세요.",
            ),
            ("user", "#Question:\n{question}"),
        ]
    )
    if prompt_type == "인스타":
        prompt = load_prompt("prompts/insta.yaml", encoding="utf-8")
    elif prompt_type == "트위터":
        prompt = load_prompt("prompts/twitter.yaml", encoding="utf-8")

    elif prompt_type == "네이버 블로그":
        prompt = load_prompt("prompts/naver.yaml", encoding="utf-8")

    elif prompt_type == "기술 블로그":
        prompt = load_prompt("prompts/tech_blog.yaml", encoding="utf-8")

    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

    # 출력파서
    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser
    return chain


# 초기화 버튼이 눌리면...
if clear_btn:
    st.session_state["messages"] = []


# 이전 대화 기록 출력
print_messages()

user_input = st.chat_input("무엇이든 물어보세요.")

# 사용자 입력 처리
if user_input:
    st.chat_message("user").write(user_input)

    # chain 생성
    chain = create_chain(selected_prompt)

    response = chain.stream({"question": user_input})

    with st.chat_message("assistant"):
        container = st.empty()

        ai_answer = ""
        for token in response:
            ai_answer += token
            container.markdown(ai_answer)

    add_message("user", user_input)
    add_message("assistant", ai_answer)
