from textblob import TextBlob

def analyze_sentiment(text):
    negative_keywords = ["슬퍼", "우울", "화나", "짜증", "불안", "지쳤어", "속상해", "힘들어"]
    positive_keywords = ["신나", "행복", "기뻐", "즐거워", "설레", "좋아", "재밌어", "기분 좋아"]

    text = text.lower()  # 소문자 변환 (예방용)

    for word in negative_keywords:
        if word in text:
            return "부정"
    for word in positive_keywords:
        if word in text:
            return "긍정"

    return "중립"
