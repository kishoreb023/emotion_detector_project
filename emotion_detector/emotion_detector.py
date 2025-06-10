from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def emotion_predictor(text):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    
    compound = scores['compound']
    neg = scores['neg']
    neu = scores['neu']
    pos = scores['pos']
    
    if compound >= 0.05:
        dominant_emotion = 'joy'
    elif compound <= -0.05:
        anger_keywords = ['angry', 'rage', 'mad', 'furious', 'annoyed', 'hate', 'frustrated']
        if any(word in text.lower() for word in anger_keywords):
            dominant_emotion = 'anger'
        else:
            dominant_emotion = 'sadness'
    else:
        dominant_emotion = 'neutral'
    
    return {
        "scores": scores,
        "dominant_emotion": dominant_emotion
    }
if __name__ == "__main__":
    text = "I am very angry and frustrated with this situation!"
    result = emotion_predictor(text)
    print(result)
