import streamlit as st

# Function to create multiple-choice questions
def multiple_choice_question(question, options, key):
    return st.multiselect(question, options, key=key)

# Function to create radio button questions
def radio_button_question(question, options, key):
    return st.radio(question, options, key=key)

# Function to create text input questions
def text_input_question(question, key):
    return st.text_input(question, key=key)

# Function to create number input questions
def number_input_question(question, key):
    return st.number_input(question, min_value=0, step=1, key=key)

# Function to create conditional text input
def conditional_text_input(question, condition, key):
    if condition:
        return st.text_input(question, key=key)

# Function to create Likert scale questions
def likert_scale_question(question, options, key):
    return st.radio(question, options, key=key)