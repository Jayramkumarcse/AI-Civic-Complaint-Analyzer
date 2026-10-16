import re

def extract_location(text):

    locations = [
        "Patna",
        "Kankarbagh",
        "Danapur",
        "Gaya",
        "Muzaffarpur",
        "Bhagalpur"
    ]

    for location in locations:
        if location.lower() in text.lower():
            return location

    return "Unknown"