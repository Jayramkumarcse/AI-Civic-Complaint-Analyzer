import joblib

# Load trained model
model = joblib.load("models/complaint_classifier.pkl")

while True:
    complaint = input("Enter complaint: ")

    if complaint.lower() == "exit":
        break

    prediction = model.predict([complaint])[0]

    print(f"\nPredicted Category: {prediction}\n")