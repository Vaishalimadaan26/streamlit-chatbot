import streamlit as st

st.title("🤖 Simple Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# user input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # simple bot logic
    if "hello" in user_input.lower():
        response = "Hi! How can I help you?"
    elif "name" in user_input.lower():
        response = "I am a Streamlit chatbot 🤖"
    else:
        response = "That's interesting! Tell me more."

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
