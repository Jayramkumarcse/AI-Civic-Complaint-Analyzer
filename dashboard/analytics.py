import streamlit as st
import pandas as pd

st.title("Complaint Analytics Dashboard")

df = pd.read_csv("data/complaints.csv")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Complaints", len(df))

with col2:
    st.metric("Unique Categories", df["category"].nunique())

st.subheader("Category Distribution")
st.bar_chart(df["category"].value_counts())

st.subheader("Complaint Dataset")
st.dataframe(df)