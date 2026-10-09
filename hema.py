
import streamlit as st
import numpy as np
import pandas as pd
import joblib

from login import login, logout
from dashboard import show_dashboard
import importlib
import database

importlib.reload(database)
from recomandation import get_recommendation

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Performance Prediction System",
    page_icon="🎓",
    layout="wide"
)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN ----------------
if not st.session_state.logged_in:
    login()
    st.stop()

logout()

# ---------------- LOAD MODEL ----------------
model = joblib.load("model.pkl")

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")

st.sidebar.success(
    f"Logged in as\n\n{st.session_state['username']}\n({st.session_state['role']})"
)

page = st.sidebar.radio(
    "Select Page",
    [
        "🏠 Home",
        "🎯 Prediction",
        "📊 Dashboard",
        "ℹ About"
    ]
)

# =====================================================
# HOME
# =====================================================

if page == "🏠 Home":

    st.title("🎓 Student Performance Prediction System")

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=150
    )

    st.markdown("""
    ### Welcome

    This AI application predicts student performance using Machine Learning.

    ### Technologies

    - Python
    - Streamlit
    - Scikit-Learn
    - Pandas
    - NumPy
    - SQLite
    - Plotly

    Use the left menu to navigate through the application.
    """)

# =====================================================
# PREDICTION
# =====================================================

elif page == "🎯 Prediction":

    st.title("🎯 Student Performance Prediction")

    st.subheader("Student Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Student Name")
        roll = st.text_input("Roll Number")
        email = st.text_input("Email")
        mobile = st.text_input("Mobile Number")

    with col2:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        branch = st.selectbox(
            "Branch",
            [
                "CSE",
                "AI & ML",
                "Data Science",
                "Cyber Security",
                "ECE",
                "EEE",
                "Mechanical",
                "Civil"
            ]
        )

        year = st.selectbox(
            "Year",
            [
                "1st Year",
                "2nd Year",
                "3rd Year",
                "4th Year"
            ]
        )

        semester = st.selectbox(
            "Semester",
            [
                "Semester 1",
                "Semester 2",
                "Semester 3",
                "Semester 4",
                "Semester 5",
                "Semester 6",
                "Semester 7",
                "Semester 8"
            ]
        )

    st.markdown("---")

    st.subheader("Academic Details")

    study = st.slider("Study Hours", 0, 12, 5)
    attendance = st.slider("Attendance (%)", 0, 100, 80)
    previous = st.slider("Previous Marks", 0, 100, 70)
    assignments = st.slider("Assignments Completed", 0, 10, 5)
    sleep = st.slider("Sleep Hours", 0, 10, 7)

    internet = st.selectbox(
        "Internet Access",
        ["Yes", "No"]
    )

    activities = st.selectbox(
        "Extra Curricular Activities",
        ["Yes", "No"]
    )

    if st.button("Predict Performance"):

        if name == "" or roll == "":
            st.warning("Please enter Student Name and Roll Number.")

        else:

            input_data = np.array([[
                study,
                attendance,
                previous,
                assignments,
                sleep
            ]])

            score = float(model.predict(input_data)[0])

            # Save to Database
            database.save_prediction(
                name,
                study,
                attendance,
                previous,
                assignments,
                sleep,
                score
            )

            st.success(f"Predicted Score : {score:.2f}")

            if score >= 90:
                performance = "Excellent 🏆"
            elif score >= 75:
                performance = "Very Good 🥇"
            elif score >= 60:
                performance = "Good 🥈"
            elif score >= 40:
                performance = "Average 🥉"
            else:
                performance = "Needs Improvement ❌"

            st.subheader("Performance")
            st.info(performance)

            st.subheader("AI Recommendation")
            st.success(get_recommendation(score))

            summary = pd.DataFrame({
                "Field": [
                    "Student Name",
                    "Roll Number",
                    "Branch",
                    "Year",
                    "Semester",
                    "Study Hours",
                    "Attendance",
                    "Previous Marks",
                    "Assignments",
                    "Sleep Hours",
                    "Predicted Score",
                    "Performance"
                ],
                "Value": [
                    name,
                    roll,
                    branch,
                    year,
                    semester,
                    study,
                    attendance,
                    previous,
                    assignments,
                    sleep,
                    round(score, 2),
                    performance
                ]
            })

            st.subheader("Prediction Summary")
            st.table(summary)

            st.balloons()

# =====================================================
# DASHBOARD
# =====================================================

elif page == "📊 Dashboard":
    show_dashboard()

# =====================================================
# ABOUT
# =====================================================

elif page == "ℹ About":

    st.title("About")

    st.markdown("""
    ## Student Performance Prediction System

    This project predicts the performance of students using Machine Learning.

    ### Features

    - Student Login
    - Performance Prediction
    - Dashboard
    - Recommendation System
    - Prediction History
    - SQLite Database

    ### Developed Using

    - Python
    - Streamlit
    - Scikit-Learn
    - Pandas
    - NumPy
    - SQLite
    """)