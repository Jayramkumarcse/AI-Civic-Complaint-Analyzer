import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv("data/complaints.csv")

# Train model
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(data["complaint"], data["category"])

# Save model
joblib.dump(model, "models/complaint_classifier.pkl")

print("Model trained successfully!")