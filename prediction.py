import streamlit as st
from preprocess import model

def app():
    st.header("Welcome to prediction page")
    st.subheader("Select values:")

    age = st.slider("Age", 0, 100)
    bmi = st.slider("BMI", 10.0, 35.0)
    children = st.slider("Children", 0, 10)
    region = st.selectbox("Region", ["northwest", "northeast", "southeast", "southwest"])
    sex = st.radio("Sex", ["Male", "Female"])
    smoker = st.radio("Somker", ["Yes", "No"])

    if (region == "northwest"):
        region = 0
    elif (region == "northeast"):
        region = 1
    elif (region == "southeast"):
        region = 2
    else:
        region = 3

    if (sex == "Male"):
        sex = 0
    else:
        sex = 1

    if (smoker == "No"):
        smoker = 0
    else:
        smoker = 1

    feature = [[age, sex, bmi, children, smoker, region]]

    if (st.button("Predict")):
        my_model, acc = model()
        prediction = my_model.predict(feature)

        st.success("Predicted successfully")
        st.success(f"Charges value is {round(prediction[0], 2)}")
        st.info(f"Our model accuracy is {round(acc, 2)}")