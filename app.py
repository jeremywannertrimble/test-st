import streamlit as st

st.title('Welcome to the Test Streamlit App')

st.write('This is a simple Streamlit app for testing purposes.')

slider_value = st.slider('Select a value', 0, 100, 50)
st.write(f'The selected value is {slider_value}.') 