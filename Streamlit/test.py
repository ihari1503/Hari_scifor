import streamlit as st
st.title("MY FIRST APP")
date = st.slider("Enter the date ",1,30,15)
st.write("Today is", date)
st.button("Say hello",type="primary")
st.image("sun.jpg",caption="Sunsets are nature's most precious gift")