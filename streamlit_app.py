import streamlit as st
# streamlit run xxxxx.py


#name = user || assistant
#avatar any .svg
with st.chat_message(name="user"):
    st.write("hello 😄")

with st.chat_message(name="assistant"):
    st.write("hello 😄")