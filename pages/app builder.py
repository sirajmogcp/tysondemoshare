import streamlit as st
import streamlit.components.v1 as components
container =st.container()

with container:
    components.iframe("https://tysonbuddy-6wrzm5zybq-uc.a.run.app/", height=1000)

st.write("Check out this [Tyson Buddy](https://tysonbuddy-6wrzm5zybq-uc.a.run.app)")
