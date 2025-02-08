import streamlit as st
import json
import os
import random
from openai import OpenAI
import time

# Get absolute path relative to the script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")  # Assuming `data/` is outside `app/`
DATA_FILE = os.path.join(DATA_DIR, "cs_curriculum.json")

# Ensure the data directory and file exist
if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(f"Data file not found: {DATA_FILE}")

# Load JSON data
with open(DATA_FILE, "r") as file:
    curriculum_data = json.load(file)

print("Successfully loaded curriculum data!")


# Initialize OpenAI client (Ensure API key is set in environment variables or secrets)
client = OpenAI(api_key="")

# Flatten curriculum into a list of topics
# Flatten curriculum into a list of topics
courses = []
for category, course_list in curriculum_data["curriculum"].items():
    for course in course_list:
        courses.append({
            "name": course["course_name"],
            "topic": course["course_name"].split(":")[0],  # Extract main topic
        })

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "current_topic" not in st.session_state:
    st.session_state.current_topic = ""

st.title("Computer Science Concept Quiz")

# Function to generate a simpler AI-powered question
def generate_question():
    course = random.choice(courses)
    topic = course["topic"]
    
    prompt = f"Generate a general computer science quiz question based on the topic '{topic}'. Keep it concise and avoid complex wording. Do not include multiple-choice options or answers."
    with st.spinner("Generating question..."):
        time.sleep(1)  # Simulate loading
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "You are a confused student who is not very confident about computer science topics. You sometimes make mistakes and ask for clarification. Your responses should be informal, uncertain, and sometimes incorrect. Use phrases like 'I think...', 'Maybe it's like...', or 'Wait, am I getting this right?'"},
                      {"role": "user", "content": prompt}]
        )
        
    question_text = response.choices[0].message.content.strip()
    return question_text, topic

# Generate a new question if needed
if st.session_state.current_question is None:
    st.session_state.current_question, st.session_state.current_topic = generate_question()
    st.session_state.chat_log.append({"role": "assistant", "content": st.session_state.current_question})

# Display chat log
for message in st.session_state.chat_log:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_answer = st.text_area("Your Answer:")

if st.button("Submit"):
    st.session_state.chat_log.append({"role": "user", "content": user_answer})
    
    prompt_eval = f"Evaluate this answer to the question: '{st.session_state.current_question}'. Answer: {user_answer}. Instead of correcting the user, ask follow-up questions that highlight gaps in their understanding and encourage deeper thinking. Do not provide the correct answer."
    with st.spinner("Thinking..."):
        time.sleep(1)  # Simulate loading
        eval_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "You are a confused student who isn't sure if they understand the topic. Instead of providing corrections, ask the user additional questions to encourage deeper thinking and help them identify gaps in their understanding."},
                      {"role": "user", "content": prompt_eval}]
        )
        
    feedback = eval_response.choices[0].message.content.strip()
    st.session_state.chat_log.append({"role": "assistant", "content": feedback})

if st.button("Next Question"):
    st.session_state.current_question, st.session_state.current_topic = generate_question()
    st.session_state.chat_log.append({"role": "assistant", "content": st.session_state.current_question})
    
st.write(f"Your Score: {st.session_state.score}")

# # Flatten curriculum into a list of topics
# courses = []
# for category, course_list in curriculum_data["curriculum"].items():
#     for course in course_list:
#         courses.append({
#             "name": course["course_name"],
#             "topic": course["course_name"].split(":")[0],  # Extract main topic
#             "url": course.get("url", ""),
#         })

# # Initialize session state
# if "score" not in st.session_state:
#     st.session_state.score = 0
# if "current_question" not in st.session_state:
#     st.session_state.current_question = None
# if "correct_answer" not in st.session_state:
#     st.session_state.correct_answer = ""
# if "current_topic" not in st.session_state:
#     st.session_state.current_topic = ""

# st.title("Computer Science Concept Quiz")

# # Function to generate an AI-powered question
# def generate_question():
#     course = random.choice(courses)
#     topic = course["topic"]
    
#     prompt = f"Generate an in-depth, conceptual computer science quiz question based on the topic '{topic}'."
#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "system", "content": "You are a CS instructor creating challenging conceptual quiz questions."},
#                   {"role": "user", "content": prompt}]
#     )
    
#     question_text = response.choices[0].message.content
    
#     return question_text, topic

# # Generate a new question if needed
# if st.session_state.current_question is None:
#     st.session_state.current_question, st.session_state.current_topic = generate_question()

# st.write(st.session_state.current_question)
# user_answer = st.text_area("Your Answer:")

# if st.button("Submit"):
#     prompt_eval = f"Evaluate this answer to the question: '{st.session_state.current_question}'.\nAnswer: {user_answer}.\nProvide feedback and correctness evaluation."
#     eval_response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "system", "content": "You are a CS instructor grading answers and providing feedback."},
#                   {"role": "user", "content": prompt_eval}]
#     )
    
#     feedback = eval_response.choices[0].message.content
#     st.write("### Feedback:")
#     st.write(feedback)
    
#     # Generate a new question
#     st.session_state.current_question, st.session_state.current_topic = generate_question()
    
# st.write(f"Your Score: {st.session_state.score}")


# import streamlit as st
# from openai import OpenAI
# import os

# def main():
#     st.title("Chatbot using OpenAI and Streamlit")
    
#     # Set API Key securely
#     api_key = "
#     if not api_key:
#         st.error("Please set your OpenAI API key in Streamlit secrets or environment variables.")
#         return
    
#     # openai.api_key = api_key
#     client = OpenAI(api_key = "
    
#     # Initialize chat history
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
    
#     # Display chat history
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])
    
#     # User input
#     user_input = st.chat_input("Type your message...")
#     if user_input:
#         # Append user message to chat history
#         st.session_state.messages.append({"role": "user", "content": user_input})
#         with st.chat_message("user"):
#             st.markdown(user_input)
        
#         # Generate response from OpenAI
#         response = client.chat.completions.create(
#           model="gpt-4o",
#           messages=st.session_state.messages
#         )
#         bot_reply = response.choices[0].message.content
        
#         # Append assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": bot_reply})
#         with st.chat_message("assistant"):
#             st.markdown(bot_reply)

# if __name__ == "__main__":
#     main()
