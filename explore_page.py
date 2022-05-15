import streamlit as st
from PIL import Image


def explore_page():
    confusion = Image.open("./images/confusion_l.png")
    bar_chart = Image.open("./images/accuracy.png")
    binary_class = Image.open("./images/Binary.png")
    st.title("Explore")
    st.subheader("Confusion Matrix (Training set)")
    st.image(confusion)
    st.subheader("Bar Chart")
    st.image(bar_chart)
    st.subheader("Binary Classification")
    st.image(binary_class)

