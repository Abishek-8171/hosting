import streamlit as st


a = st.text_input('Enter your name')

b = st.button('press')

if b:
    st.write(f'Hi {a} have a nice day')