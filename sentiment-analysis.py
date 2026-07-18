from textblob import TextBlob

reviews = [
    "This product is amazing",
    "I love this phone",
    "Worst experience ever",
    "Very bad quality",
    "It is okay",
    "Excellent service",
    "Not worth the money"
]

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

print("Sentiment Analysis Results:\n")

for review in reviews:
    sentiment = get_sentiment(review)
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}")
    print("-" * 30)