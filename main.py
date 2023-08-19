import streamlit as st

st.header("weather forcast for the next days")
place = st.text_input("place")
temp = st.slider("enter temp value", 1, 5)
option = st.selectbox("select data to view", ('temperature', 'sky'))
st.subheader(f"{option} for the next {temp} days {place}")
