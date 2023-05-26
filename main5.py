import streamlit as st

def chatbot():
    st.title("Chatbot")
    user_input = st.text_input("You:")
    if st.button("Send"):
        if user_input:
            st.text("Bot: " + user_input)
        else:
            st.text("Bot: Please enter something.")

if __name__ == "__main__":
    chatbot()
