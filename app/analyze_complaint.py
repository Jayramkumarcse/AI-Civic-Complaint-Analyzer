import joblib
from textblob import TextBlob

model = joblib.load("models/complaint_classifier.pkl")

while True:

    complaint = input("Enter complaint: ")

    if complaint.lower() == "exit":
        break

    category = model.predict([complaint])[0]

    sentiment_score = TextBlob(complaint).sentiment.polarity

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print("\nAnalysis Result")
    print("----------------")
    print("Category :", category)
    print("Sentiment:", sentiment)