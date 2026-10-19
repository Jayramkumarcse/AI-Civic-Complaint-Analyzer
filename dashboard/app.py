import pandas as pd
import streamlit as st
import joblib
from textblob import TextBlob

model = joblib.load("models/complaint_classifier.pkl")

st.title("AI Civic Complaint Analyzer")

complaint = st.text_area("Enter Complaint")

if st.button("Analyze") and complaint:

    category = model.predict([complaint])[0]

    probabilities = model.predict_proba([complaint])[0]
    confidence = max(probabilities) * 100

    negative_words = [
    "accident",
    "fire",
    "injury",
    "death",
    "hospital",
    "garbage",
    "overflow",
    "outage",
    "damage",
    "broken",
    "contamination",
    "pothole",
    "sewage",
    "leakage"
]

sentiment = "Neutral"

for word in negative_words:
    if word in complaint.lower():
        sentiment = "Negative"
        break

    priority = "Low"

    if any(word in complaint.lower() for word in [
        "hospital",
        "accident",
        "burst",
        "fire",
        "death",
        "emergency"
    ]):
        priority = "High"

    location = "Unknown"

    known_locations = [
        "Patna",
        "Kankarbagh",
        "Danapur",
        "Gaya",
        "Muzaffarpur",
        "Bhagalpur"
    ]

    for place in known_locations:
        if place.lower() in complaint.lower():
            location = place
            break

    st.success(f"Category: {category}")
    st.info(f"Confidence: {confidence:.2f}%")
    st.info(f"Sentiment: {sentiment}")
    st.warning(f"Priority: {priority}")
    st.write(f"Location: {location}")

    new_row = pd.DataFrame([{
        "complaint": complaint,
        "category": category,
        "priority": priority,
        "location": location
    }])

    new_row.to_csv(
        "data/complaint_history.csv",
        mode="a",
        header=False,
        index=False
    )

    st.success("Complaint saved successfully!")