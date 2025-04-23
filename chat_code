import streamlit as st

# Function to get bot responses based on predefined rules
def get_response(user_input):
    responses = {
        "hello": "Hello! How can I assist you today?",
        "courses": "We offer the following courses: Computer Science, Electrical Engineering, Mechanical Engineering, etc.",
        "admission": "To apply for admission, visit our admissions page and submit the required documents.",
        "fees": "The fee structure is available on the website under the 'Fees' section.",
        "library": "The library is open from 9 AM to 6 PM every day, except on holidays.",
        "schedule": "You can check the class schedule on the student portal."
    }
    # Default response if input is not found in predefined rules
    return responses.get(user_input.lower(), "I'm sorry, I didn't understand that. Can you please ask something else?")

# Streamlit UI for chatbot interaction
def chatbot_interface():
    st.title("College Chatbot")
    st.write("Ask me about courses, admission, fees, or anything related to the college!")
    
    user_input = st.text_input("You: ", "")
    if user_input:
        # Get bot response based on user input
        bot_response = get_response(user_input)
        st.write(f"Bot: {bot_response}")

# Run the app
if __name__ == "__main__":
    chatbot_interface()
