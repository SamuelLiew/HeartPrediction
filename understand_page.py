import streamlit as st
from PIL import Image


def understand_page():
    bmi_image = Image.open("./images/BMIChart.jpeg")
    obesity_image = Image.open('./images/RateOfObesity.jpg')
    heart_image = Image.open("./images/HeartDisease.jpg")
    st.title("Understand")
    st.subheader("Should I see a doctor?")
    st.text("Since this is a life threatening disease, it would be wise to get a check up if you")
    st.text("feel like you're sick.")
    st.text("You should get a check up if the prediction predicted that you have at least 50% chance of hacing heart disease.")
    st.text("chance of hacing heart disease.")
    st.subheader("What is my BMI?")
    st.image(bmi_image)
    st.subheader("Rate of Obesity?")
    st.image(obesity_image)
    st.subheader("What is Heart Disease?")
    st.image(heart_image)
