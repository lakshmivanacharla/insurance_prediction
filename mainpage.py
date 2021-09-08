import streamlit as st
import prediction

st.title("My insurance prediction app")
st.markdown("### This web uses Linear Regression to predict values")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", ["Home", "Prediction"])

if (page == "Prediction"):
    prediction.app()
