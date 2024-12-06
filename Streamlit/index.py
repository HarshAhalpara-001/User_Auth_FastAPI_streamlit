import streamlit as st
import requests

# Backend URL
BASE_URL = "http://127.0.0.1:8000"  # Update this to your FastAPI backend URL

# Session state to store authentication details
if "access_token" not in st.session_state:
    st.session_state["access_token"] = None

# Authentication functions
def login(username, password):
    """Authenticate user by sending credentials to the FastAPI login endpoint."""
    try:
        # Use form data instead of JSON
        response = requests.post(
            f"{BASE_URL}/login",
            data={"username": username, "password": password},  # form data
        )
        if response.status_code == 200:
            data = response.json()
            st.session_state["access_token"] = data["access_token"]
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")
    except Exception as e:
        st.error(f"An error occurred: {e}")


def register(username, password):
    """Register a new user by sending details to the FastAPI register endpoint."""
    try:
        response = requests.post(
            f"{BASE_URL}/register",
            json={"username": username, "password": password},
        )
        if response.status_code == 200:
            st.success("User registered successfully! Please login.")
        else:
            st.error(response.json().get("detail", "Registration failed"))
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Define pages
def login_page():
    st.title("Login")
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        login(login_username, login_password)

def register_page():
    st.title("Register")
    register_username = st.text_input("Username", key="register_username")
    register_password = st.text_input("Password", type="password", key="register_password")
    if st.button("Register"):
        register(register_username, register_password)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login", "Register"])

if st.session_state["access_token"]:
    st.success("You are logged in!")
    if st.sidebar.button("Logout"):
        st.session_state["access_token"] = None
        st.success("Logged out successfully!")
else:
    # Render the selected page
    if page == "Login":
        login_page()
    elif page == "Register":
        register_page()
