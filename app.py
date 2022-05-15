import streamlit as st
from predict_page import predict_page
from explore_page import explore_page
from understand_page import understand_page

selection = st.sidebar.selectbox("Explore Or Predict", ("🧠 Predict", "🔍 Explore", "🧐 Understand"))
if selection == "🧠 Predict":
    predict_page()
elif selection == "🔍 Explore":
    explore_page()
else:
    understand_page()
