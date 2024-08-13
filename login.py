import streamlit as st
from navigation import make_sidebar

#if "logged_in" not in st.session_state:
 #   st.session_state.logged_in = False

make_sidebar()

st.title("Welcome to the Packing Portal")
st.write("Please log in to continue")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button('Submit')

if submit_button:
     if username == "phone" and password == "hellokitty":
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        st.switch_page("cust.py")            
        st.experimental_rerun()  # Reload the page to reflect the login state
    elif username == "laptop" and password == "chamberofsecrets":
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
          # should show filtered views, so take them to different pages and tables            
        st.experimental_rerun()  # Reload the page to reflect the login state
        st.switch_page("operations.py")
        st.experimental_rerun()  # Reload the page to reflect the login state
    elif username == "hehe" and password == "helloworld":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            st.experimental_rerun()  # Reload the page to reflect the login state
            st.switch_page("basicUser.py")
            st.experimental_rerun()  # Reload the page to reflect the login state
    else:
        st.error("Incorrect username or password")

        
