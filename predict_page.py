import math
import pickle
import numpy as np
import streamlit as st


def load_model():
    with open("saved_data.pkl", "rb") as file:
        pickle_data = pickle.load(file)
        return pickle_data


data = load_model()
svc = data["model"]
le_health = data["le_health"]
le_sex = data["le_sex"]
le_age = data["le_age"]
le_race = data["le_race"]


def predict_page():
    st.title("Heart Disease Prediction (91% Accuracy)")
    st.write("""### We need some information""")

    gender_choice = (
        "Male",
        "Female"
    )

    health_choice = (
        "Excellent",
        "Very Good",
        "Good",
        "Fair",
        "Poor"
    )

    race_choice = (
        "White",
        "Black",
        "Hispanic",
        "Asian",
        "American Indian/ Alaskan Native",
        "Other"
    )

    choice = (
        "No",
        "Yes"

    )

    gender = st.selectbox("Gender", gender_choice)
    race = st.selectbox("Race", race_choice)
    health = st.selectbox("General Health", health_choice)
    smoke = st.selectbox("History of Smoking", choice)
    alcohol = st.selectbox("History of Alcoholism", choice)
    stroke = st.selectbox("History of Stroke", choice)
    diffwalking = st.selectbox("Difficulty Walking", choice)
    diabetic = st.selectbox("Diabetic", choice)
    physical = st.selectbox("Physical Activities/Exercise", choice)
    asthma = st.selectbox("Asthma", choice)
    kidney = st.selectbox("History of Kidney Disease", choice)
    skin = st.selectbox("History of Skin Cancer", choice)
    bmi = st.number_input("Body Mass Index", step=0.1)
    sleeptime = st.slider("Amount of Sleep", 4, 12, 8)
    age = st.slider("Age", 18, 100, 50)

    submit = st.button("Predict")

    def convert(input_array):
        input_array[:, 5] = le_sex.transform(input_array[:, 5])
        input_array[:, 6] = le_age.transform(input_array[:, 6])
        input_array[:, 7] = le_race.transform(input_array[:, 7])
        input_array[:, 10] = le_health.transform(input_array[:, 10])
        output = input_array.astype(float)
        return output

    def age_converter(input_age):
        if 18 <= input_age <= 39:
            return "18-39"
        elif 40 <= input_age <= 59:
            return "40-59"
        elif 60 <= input_age <= 79:
            return "60-79"
        else:
            return "80 or older"

    if submit:
        choice_map = {"Yes": 1, "No": 0}
        array = np.array([[bmi, choice_map[smoke], choice_map[alcohol], choice_map[stroke], choice_map[diffwalking],
                           gender, age_converter(age), race, choice_map[diabetic], choice_map[physical], health,
                           sleeptime, choice_map[asthma], choice_map[kidney], choice_map[skin]]])
        converted_array = convert(array)
        heart_disease = svc.predict(converted_array)
        heart_disease_probability = svc.predict_proba(converted_array)

        if heart_disease == 1:
            st.subheader("You might have Heart Disease")
        else:
            st.subheader("You might not have Heart Disease")
        st.subheader(f"{math.floor(heart_disease_probability[0][-1]*100)}% chance of having heart disease")
