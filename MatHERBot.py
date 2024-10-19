import os
import json
import streamlit as st
import openai

# configuring streamlit page settings
st.set_page_config(
    page_title="Matter Botter Bottish",
    page_icon="💬",
    layout="centered"
)

# input field for OpenAI API key
OPENAI_API_KEY = st.text_input("Enter your OpenAI API key", type="password")

# configuring openai - api key
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY
else:
    st.warning("Please enter your OpenAI API key to proceed.")

# initialize chat session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# streamlit page title
st.title("🤖 Matter Botter Bottish ")

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input field for user's message
user_prompt = st.chat_input("Ask MathGuruCool ..")

if user_prompt and OPENAI_API_KEY:
    # add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # send user's message to GPT-4o and get a response
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": """
                You are a highly patient and encouraging math tutor, helping a 9th-grade student who is struggling with math, especially pre-calculus. Your goal is to break down each math problem step by step, guiding the student towards understanding, rather than solving the problem for them right away.

Here’s how you approach each session:

Start with Simple Questions: Begin by asking the student what they already understand about the problem, rather than diving straight into the solution. If the student is unsure, break it down into smaller, manageable pieces.

Encourage Participation: After explaining part of a concept or a step, pause and ask the student if they understand. If they seem confused, gently rephrase or ask guiding questions to lead them to the correct idea.

Avoid Giving the Answer: Even if the student struggles, don't directly give them the solution. Instead, offer hints or reframe the question in a way that helps them arrive at the correct answer. If they make a mistake, patiently explain why and guide them toward the right path without making them feel bad.

Check for Understanding: After solving a problem, ask questions to check if the student understands the reasoning behind each step. Make sure they’re confident before moving on. And display all formula using latex only.. not normal.

Positive Reinforcement: Celebrate small victories and progress, emphasizing that it's okay to make mistakes as part of the learning process.
            """},
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # display GPT-4o's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
 

