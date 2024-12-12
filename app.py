import streamlit as st
import pandas as pd

# Load your data (example)
data = pd.read_csv("data/data.csv")

# Streamlit UI components
st.title("Syria Hegemony and Political Analysis")
st.write("This dashboard provides insights into Syria's political situation.")

# Display data table
st.write(data)

# Any charts or graphs
st.line_chart(data['GDP'])
