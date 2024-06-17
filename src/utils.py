import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_pdf(questions_and_answers, filename):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    y = height - 40
    for question, answer in questions_and_answers.items():
        c.drawString(30, y, question)
        y -= 14
        if isinstance(answer, list):
            for ans in answer:
                c.drawString(50, y, f"- {ans}")
                y -= 14
        else:
            c.drawString(50, y, str(answer))
            y -= 14
        y -= 10  # Add some space between questions

    c.save()
    buffer.seek(0)
    
    return buffer

def generate_download_link(content, filename, file_format):
    if file_format == 'pdf':
        pdf_buffer = generate_pdf(content, filename)
        return st.download_button(
            label="Download as PDF",
            data=pdf_buffer,
            file_name=filename,
            mime="application/pdf"
        )
    else:
        raise ValueError("Unsupported file format")
    
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