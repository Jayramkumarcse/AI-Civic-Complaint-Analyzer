def get_priority(complaint):

    complaint = complaint.lower()

    high_words = [
        "accident",
        "hospital",
        "fire",
        "death",
        "burst",
        "injury",
        "emergency",
        "outage"
    ]

    medium_words = [
        "leakage",
        "garbage",
        "pothole",
        "traffic"
    ]

    for word in high_words:
        if word in complaint:
            return "High"

    for word in medium_words:
        if word in complaint:
            return "Medium"

    return "Low"