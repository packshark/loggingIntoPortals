import streamlit as st
from time import sleep
from navigation import make_sidebar

make_sidebar()

st.title("Welcome to the Packing Portal")

st.write("Please log in to continue")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "phone" and password == "hellokitty":
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("cust.py")
    elif username == "laptop" and password == "chamberofsecrets":
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
      # should show filtered views, so take them to different pages and tables
        st.switch_page("operations.py")
    elif username == "hehe" and password == "helloworld":
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("basicUser.py")
    else:
        st.error("Incorrect username or password")
