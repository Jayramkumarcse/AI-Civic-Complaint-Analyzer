from app.priority_engine import get_priority
from app.location_detector import extract_location
import streamlit as st
import joblib
from textblob import TextBlob

model = joblib.load("models/complaint_classifier.pkl")

st.title("AI Civic Complaint Analyzer")

complaint = st.text_area("Enter Complaint")

if st.button("Analyze"):

    category = model.predict([complaint])[0]

probabilities = model.predict_proba([complaint])[0]
confidence = max(probabilities) * 100
st.success(f"Category: {category}")
st.info(f"Confidence: {confidence:.2f}%")
    polarity = TextBlob(complaint).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    st.success(f"Category: {category}")
    st.info(f"Sentiment: {sentiment}")
priority = "Low"

high_priority_words = [
    "accident",
    "hospital",
    "emergency",
    "fire",
    "burst",
    "death",
    "injury"
]
priority = "Low"

high_priority_words = [
    "accident",
    "hospital",
    "emergency",
    "fire",
    "burst",
    "death",
    "injury",
    "leakage"
]

for word in high_priority_words:
    if word in complaint.lower():
        priority = "High"
        break

st.warning(f"Priority: {priority}")
for word in high_priority_words:
    if word in complaint.lower():
        priority = "High"
        break

st.warning(f"Priority: {priority}")