import streamlit as st
import pandas as pd
import joblib


# LOAD MODEL
model = joblib.load(
    "models/dropout_model.pkl"
)


# TITLE
st.title(
    "Student Dropout Prediction System"
)

st.write(
    "Predict students at risk of dropping out"
)


# INPUTS
age = st.slider(
    "Age",
    15,
    25
)

studytime = st.slider(
    "Study Time",
    1,
    10
)

failures = st.slider(
    "Failures",
    0,
    5
)

absences = st.slider(
    "Absences",
    0,
    100
)

G1 = st.slider(
    "G1 Grade",
    0,
    20
)

G2 = st.slider(
    "G2 Grade",
    0,
    20
)


# CREATE DATAFRAME
input_data = pd.DataFrame({
    "age": [age],
    "studytime": [studytime],
    "failures": [failures],
    "absences": [absences],
    "G1": [G1],
    "G2": [G2]
})


# PREDICT BUTTON
if st.button("Predict"):

    prediction = model.predict(
        input_data
    )

    if prediction[0] == 1:

        st.error(
            "High Dropout Risk"
        )

    else:

        st.success(
            "Low Dropout Risk"
        )