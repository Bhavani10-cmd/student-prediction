import streamlit as st
from database import create_database, register_user, login_user

# Create database automatically
create_database()


def login():

    tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])

    # ---------------- LOGIN ----------------
    with tab1:

        st.title("🎓 Student Performance Prediction System")
        st.subheader("Login")

        username = st.text_input(
            "Username",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button("Login"):

            if username == "" or password == "":
                st.warning("Please enter username and password.")

            else:

                user = login_user(username, password)

                if user:

                    st.session_state.logged_in = True
                    st.session_state.username = user[1]
                    st.session_state.role = user[3]

                    st.success("Login Successful ✅")
                    st.rerun()

                else:

                    st.error("Invalid Username or Password")

    # ---------------- REGISTER ----------------
    with tab2:

        st.title("📝 Register New User")

        new_username = st.text_input(
            "Create Username",
            key="register_username"
        )

        new_password = st.text_input(
            "Create Password",
            type="password",
            key="register_password"
        )

        role = st.selectbox(
            "Role",
            ["Student", "Teacher", "Admin"]
        )

        if st.button("Register"):

            if new_username == "" or new_password == "":
                st.warning("Please fill all fields.")

            else:

                success = register_user(
                    new_username,
                    new_password,
                    role
                )

                if success:
                    st.success("Registration Successful 🎉")
                    st.info("Now login using your username and password.")

                else:
                    st.error("Username already exists.")


def logout():

    st.sidebar.markdown("---")

    if st.sidebar.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""

        st.rerun()