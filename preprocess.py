import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

@st.cache
def load_data():
    """This function return pre-processed features and target"""
    # Load the dataset
    df = pd.read_csv("./insurance (2).csv")

    # drop null values and check info.
    df = df.dropna()

    # Change the object values to numerical values for object column
    df.replace(to_replace={
        "male":0, "female":1,
        "no":0, "yes":1,
        "northwest": 0, "northeast":1, "southeast":2, "southwest":3
    }, inplace=True)

    # Split data into feature and target
    X = df.drop(['charges'], axis=1)
    y = df['charges']

    # Return values
    return X, y

@st.cache
def model():
    """This function train the model and return the accuracy/"""
    # Load features and target
    X, y = load_data()

    # Create model and get accuracy.
    model = LinearRegression()
    model.fit(X, y)
    acc = model.score(X, y)

    # return accuracy
    return model, acc