import streamlit as st
from PIL import Image


def understand_page():
    bmi_image = Image.open("./images/BMIChart.jpeg")
    obesity_image = Image.open('./images/RateOfObesity.jpg')
    heart_image = Image.open("./images/HeartDisease.jpg")
    st.title("Understand")
    st.subheader("What is my BMI?")
    st.image(bmi_image)
    st.subheader("Rate of Obesity?")
    st.image(obesity_image)
    st.subheader("What is Heart Disease?")
    st.image(heart_image)
