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