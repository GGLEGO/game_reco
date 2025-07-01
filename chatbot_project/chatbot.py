import streamlit as st
from openai import OpenAI  # ✅ 최신 방식
from utils import analyze_sentiment
from recommend import get_recommendation_by_emotion

# 🔑 OpenAI 클라이언트 초기화
client = OpenAI(api_key="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")

col1, col2 = st.columns(2)


st.title("🧠 심리 기반 추천 챗봇")

if "history" not in st.session_state:
    st.session_state["history"] = []
user_name = st.text_input("이름을 알려주세요")
user_input = st.text_input("당신의 생각이나 감정을 말해보세요:")

if user_input:
    # 감정 분석
    emotion = analyze_sentiment(user_input)

    get_name = user_name
    # GPT 응답 생성 (✅ 최신 방식으로 수정)
    gpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 따뜻하고 공감적인 심리 상담 챗봇입니다."},
            {"role": "user", "content": user_input}
        ]
    )

    assistant_reply = gpt_response.choices[0].message.content
    recommendation = get_recommendation_by_emotion(emotion)


    st.session_state["history"].append(("🤖 챗봇", assistant_reply))
    #st.session_state["history"].append(("🎁 추천", recommendation))
    st.session_state["history"].append(("👤 사용자", user_name))

# 대화 내역 출력
for speaker, text in reversed(st.session_state["history"]):
    st.markdown(f"**{speaker}:** {text}")
