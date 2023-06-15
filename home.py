import streamlit as st
from PIL import Image
st.set_page_config(layout="wide", page_title="Home", page_icon="👋")
 
image=Image.open("tyson.png")
st.image(image)
st.title("Tyson Foods GenAI Demo") 