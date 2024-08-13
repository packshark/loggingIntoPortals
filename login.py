import streamlit as st

# Main content
st.title("Welcome to the Packing Portal")
st.write("Please log in to continue")

# Display login form
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password")
    submit_button = st.form_submit_button('Submit')

