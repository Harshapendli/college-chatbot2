import streamlit as st

# Simple response function
def get_response(user_input):
    responses = {
        "hello": "Hello! How can I assist you today?",
        "courses": "We offer various courses like Computer Science, Engineering, etc."
    }
    return responses.get(user_input.lower(), "I'm sorry, I didn't understand that.")

# Streamlit interface
def chatbot_interface():
    st.title("College Chatbot")
    st.write("Ask me about courses, admission, etc!")
    
    user_input = st.text_input("You: ", "")
    if user_input:
        bot_response = get_response(user_input)
        st.write(f"Bot: {bot_response}")

# This is crucial! Make sure this is indented properly.
if __name__ == "__main__":
    chatbot_interface()
