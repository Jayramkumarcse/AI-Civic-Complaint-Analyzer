import pandas as pd

data = []

water = [
    "Water pipeline damaged near sector",
    "Drinking water unavailable in colony",
    "Low water pressure in area",
    "Water tank leakage reported",
    "No water supply since morning",
]

garbage = [
    "Garbage dumped near market",
    "Waste not collected from street",
    "Overflowing dustbin in colony",
    "Garbage causing foul smell",
    "Garbage accumulated near school",
]

electricity = [
    "Power outage in sector",
    "Transformer damaged in locality",
    "Streetlights not functioning",
    "Electric pole sparking",
    "Frequent power cuts reported",
]

road = [
    "Road damaged after heavy rain",
    "Potholes causing accidents",
    "Broken road near school",
    "Road repair required urgently",
    "Cracked road creating issues",
]

traffic = [
    "Traffic jam near hospital",
    "Signal not working properly",
    "Heavy congestion near station",
    "Traffic blockage on main road",
    "Vehicle congestion during peak hours",
]

sanitation = [
    "Drainage blockage in colony",
    "Sewage overflow on road",
    "Dirty public toilet reported",
    "Drain water accumulation",
    "Blocked sewer line issue",
]

for i in range(1, 85):
    for text in water:
        data.append([f"{text} {i}", "Water"])

    for text in garbage:
        data.append([f"{text} {i}", "Garbage"])

    for text in electricity:
        data.append([f"{text} {i}", "Electricity"])

    for text in road:
        data.append([f"{text} {i}", "Road"])

    for text in traffic:
        data.append([f"{text} {i}", "Traffic"])

    for text in sanitation:
        data.append([f"{text} {i}", "Sanitation"])

df = pd.DataFrame(data, columns=["complaint", "category"])

df.to_csv("data/complaints_large.csv", index=False)

print("Dataset created:", len(df))
