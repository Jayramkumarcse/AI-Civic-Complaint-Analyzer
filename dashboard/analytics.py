import streamlit as st
import pandas as pd

df = pd.read_csv("data/complaint_history.csv")

st.title("Complaint Analytics Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Complaints", len(df))

with col2:
    st.metric("Unique Categories", df["category"].nunique())

with col3:
    st.metric(
        "High Priority Complaints",
        len(df[df["priority"] == "High"])
    )

st.subheader("Category Distribution")
st.bar_chart(df["category"].value_counts())

st.subheader("Location Distribution")
st.bar_chart(df["location"].value_counts())

st.subheader("Recent Complaints")
st.dataframe(df.tail(10))