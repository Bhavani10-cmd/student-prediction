if page == "Prediction":

    st.title("🎓 Student Performance Prediction")

    st.subheader("Enter Student Details")

    name = st.text_input("Student Name")

    branch = st.selectbox(
        "Branch",
        ["CSE", "AI & ML", "Data Science",
         "Cyber Security", "ECE", "EEE",
         "Mechanical", "Civil"]
    )

    year = st.selectbox(
        "Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    study = st.slider("Study Hours", 0, 12, 5)

    attendance = st.slider("Attendance (%)", 0, 100, 80)

    previous = st.slider("Previous Marks", 0, 100, 70)

    assignments = st.slider("Assignments Completed", 0, 10, 5)

    sleep = st.slider("Sleep Hours", 0, 10, 7)

    if st.button("Predict Performance"):

        input_data = np.array([[study,
                                attendance,
                                previous,
                                assignments,
                                sleep]])

        score = float(model.predict(input_data)[0])

        st.success(f"Predicted Final Score: {score:.2f}")

        if score >= 90:
            st.success("Performance Level: Excellent 🏆")
        elif score >= 75:
            st.info("Performance Level: Very Good 🥇")
        elif score >= 60:
            st.warning("Performance Level: Good 🥈")
        elif score >= 40:
            st.warning("Performance Level: Average 🥉")
        else:
            st.error("Performance Level: Needs Improvement ❌")

        st.subheader("Study Recommendation")

        st.info(get_recommendation(score))

        summary = pd.DataFrame({
            "Field": [
                "Name",
                "Branch",
                "Year",
                "Study Hours",
                "Attendance",
                "Previous Marks",
                "Assignments",
                "Sleep Hours",
                "Predicted Score"
            ],
            "Value": [
                name,
                branch,
                year,
                study,
                attendance,
                previous,
                assignments,
                sleep,
                round(score, 2)
            ]
        })

        st.subheader("Student Summary")

        st.table(summary)

        st.balloons()