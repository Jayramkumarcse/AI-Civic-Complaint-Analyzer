import streamlit as st
import pandas as pd

st.title("Complaint Analytics Dashboard")

df = pd.read_csv("data/complaints.csv")

st.metric("Total Complaints", len(df))

st.subheader("Category Distribution")

category_counts = df["category"].value_counts()

st.bar_chart(category_counts)