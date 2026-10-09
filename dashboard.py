import streamlit as st
import pandas as pd
import plotly.express as px


def show_dashboard():

    st.header("📊 Student Analytics Dashboard")

    try:
        data = pd.read_csv("student_performance.csv")

    except:
        st.error("Dataset not found!")
        return

    st.subheader("Dataset Preview")

    st.dataframe(data)

    st.subheader("Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Students", len(data))
    col2.metric("Average Score", round(data["FinalScore"].mean(), 2))
    col3.metric("Highest Score", data["FinalScore"].max())

    st.divider()

    st.subheader("Study Hours vs Final Score")

    fig = px.scatter(
        data,
        x="StudyHours",
        y="FinalScore",
        color="Attendance",
        size="Assignments",
        hover_data=["PreviousMarks"]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Attendance Distribution")

    fig = px.histogram(
        data,
        x="Attendance",
        nbins=10
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Previous Marks vs Final Score")

    fig = px.line(
        data,
        x="PreviousMarks",
        y="FinalScore"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Correlation Heatmap")

    st.dataframe(data.corr(numeric_only=True))