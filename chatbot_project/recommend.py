def get_recommendation_by_emotion(emotion):
    if emotion == "positive":
        return "😊 오늘 기분이 좋아 보이네요! 활기찬 음악 플레이리스트를 추천할게요."
    elif emotion == "negative":
        return "😢 요즘 힘들어 보이네요. 마음을 다독여주는 책 하나 읽어보시는 건 어때요?"
    elif emotion == "neutral":
        return "🙂 차분한 하루군요. 따뜻한 차 한잔과 함께 명상 음악을 들어보세요."
    else:
        return "기분을 잘 모르겠어요. 조금 더 얘기해볼까요?"