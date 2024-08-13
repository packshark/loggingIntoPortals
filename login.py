import streamlit as st
from navigation import make_sidebar

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

make_sidebar()

st.title("Welcome to the Packing Portal")
st.write("Please log in to continue")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log in", type="primary"):
        if username == "phone" and password == "hellokitty":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            st.experimental_rerun()  # Reload the page to reflect the login state
            st.switch_page("cust.py")
        elif username == "laptop" and password == "chamberofsecrets":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
              # should show filtered views, so take them to different pages and tables
            st.experimental_rerun()  # Reload the page to reflect the login state
            st.switch_page("operations.py")
        elif username == "hehe" and password == "helloworld":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            st.experimental_rerun()  # Reload the page to reflect the login state
            st.switch_page("basicUser.py")
        else:
            st.error("Incorrect username or password")
