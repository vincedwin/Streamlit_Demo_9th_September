import streamlit as st
# streamlit run xxxxx.py

##Part 1
# name = user || assistant
# avatar any .svg
# with st.chat_message(name="user"):
#     st.write("hello 😄")
#
# with st.chat_message(name="assistant"):
#     st.write("hello 😄")

##Part 2
st.title("ChatBot")

if "message" not in st.session_state:
    st.session_state = []
#[
    # {"role":"user", "content":"prompt"},
    # {"role":"assistant", "content":"reply"}
# ]

#display chat history
for message in st.session_state:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

with st.chat_message(name="assistant"):
    st.write("What can i do for you😄")

prompt = st.chat_input("your message")
if prompt:
    #write into the chat history
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.append({"role":"user", "content":prompt})
    # actions
    response = f'echo {prompt}'
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.append({"role": "assistant", "content": response})

