import streamlit as st
from openai import OpenAI
from utils import analyze_sentiment
from recommend import get_recommendation_by_emotion  # 지금은 안 써도 됨

# OpenAI 클라이언트 초기화
client = OpenAI(api_key="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") 

st.title("🧠 심리 기반 게임 추천 챗봇")

# 세션 상태 초기화
if "history" not in st.session_state:
    st.session_state["history"] = []

# 사용자 입력 영역
user_name = st.text_input("이름을 알려주세요")
user_input = st.text_input("당신의 생각이나 감정을 말해보세요:")

# 🎮 플레이어 수 선택
player_count = st.selectbox("함께 플레이할 인원 수는 몇 명인가요?", options=list(range(1, 11)), index=0)

# 💰 가격 정보 입력
user_price = st.text_input("원하는 게임 가격대가 있나요? (예: 10000원, $15 등)", placeholder="예: 20000원")

if user_price:
    # 감정 분석
    emotion = analyze_sentiment(user_input)
    st.write("🔍 감정 분석 결과:", emotion)  # 디버깅용

    # GPT 응답 생성
    system_prompt = f"""당신은 다양한 게임 이름을 심리에 따라 추천해주는 챗봇입니다.
    사용자가 입력한 감정에 따라 적절한 온라인 게임을 추천합니다.
    사용자가 입력한 게임의 플레이 인원수를 정확히 고려해서 맞춤형 온라인 게임을 추천합니다.
    사용자가 입력한 가격을 정확히 계산하고 정확한 가격을 바탕으로 맞춤형 온라인 게임을 추천합니다.
    사용자가 입력한 정보를 바탕으로 정확한 온라인 게임을 추천합니다.
    사용자가 원하는 플레이 인원수는 {player_count}명이고, 희망 가격대는 '{user_price}'입니다."""

    gpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    assistant_reply = gpt_response.choices[0].message.content

    # 감정 기반 장르 추천
    if emotion == "부정":
        genre_recommendation = "🎮 힐링이 필요하시군요. 캐주얼, 힐링 게임을 추천해요!"
    elif emotion == "긍정":
        genre_recommendation = "⚔️ 지금 기분이 좋으시군요! 경쟁 게임을 즐겨보는 건 어떠세요?"
    else:
        genre_recommendation = "🤔 감정을 잘 파악할 수 없었어요. 다양한 장르를 시도해보세요!"

    # 대화 저장
    st.session_state["history"].append(("👤 사용자", f"{user_name}: {user_input}"))
    st.session_state["history"].append(("📌 조건", f"인원수: {player_count}명 / 희망 가격: {user_price}"))
    st.session_state["history"].append(("🤖 챗봇", assistant_reply))
    st.session_state["history"].append(("🎮 추천", genre_recommendation))

# 대화 기록 출력
for speaker, text in reversed(st.session_state["history"]):
    st.markdown(f"**{speaker}:** {text}")
