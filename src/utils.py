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

def display_data_and_process_question(question_num, question_text, key, services, headers):
    st.subheader(f'{question_num} {question_text}')

    # Create grid for question
    st.write(
        f"""
        <style>
        .grid-container-{key} {{
            display: grid;
            grid-template-columns: repeat({len(headers)}, 1fr);
            gap: 1px;
            background-color: #000;
        }}
        .grid-item-{key} {{
            background-color: #fff;
            padding: 10px;
            font-size: 14px;
            text-align: center;
            border: 1px solid #ddd;
        }}
        .grid-header-{key} {{
            font-weight: bold;
            background-color: #f0f0f0;
        }}
        .service-name-{key} {{
            text-align: left;
            max-width: 200px;
            word-wrap: break-word;
        }}
        </style>
        <div class="grid-container-{key}">
            <div class="grid-item-{key} grid-header-{key}">{headers[0]}</div>
            <div class="grid-item-{key} grid-header-{key}">{headers[1]}</div>
            <div class="grid-item-{key} grid-header-{key}">{headers[2]}</div>
            <div class="grid-item-{key} grid-header-{key}">{headers[3]}</div>
            <div class="grid-item-{key} grid-header-{key}">{headers[4]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for i, service in enumerate(services):
        st.write(
            f"""
            <div class="grid-container-{key}">
                <div class="grid-item-{key} service-name-{key}">{service}</div>
                <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_0"></div>
                <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_1"></div>
                <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_2"></div>
                <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_3"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

def display_integration_question(question_num, question_text, key, services, headers):
    st.subheader(f'{question_num} {question_text}')
    options = ['NO', 'SI']
    selected = st.radio('Seleziona un\'opzione:', options, key=key)

    if selected == 'SI':
        st.subheader('Seleziona le caselle relative ai servizi o alle applicazioni per i quali è in funzione l’integrazione operativa')
        
        # Create grid for question
        st.write(
            f"""
            <style>
            .grid-container-{key} {{
              display: grid;
              grid-template-columns: repeat({len(headers)}, 1fr);
              gap: 1px;
              background-color: #000;
            }}
            .grid-item-{key} {{
              background-color: #fff;
              padding: 10px;
              font-size: 14px;
              text-align: center;
              border: 1px solid #ddd;
            }}
            .grid-header-{key} {{
              font-weight: bold;
              background-color: #f0f0f0;
              word-wrap: break-word;
              overflow-wrap: break-word;
              white-space: pre-wrap;
            }}
            .service-name-{key} {{
              text-align: left;
              max-width: 200px;
              word-wrap: break-word;
            }}
            </style>
            <div class="grid-container-{key}">
              <div class="grid-item-{key} grid-header-{key}">{headers[0]}</div>
              <div class="grid-item-{key} grid-header-{key}">{headers[1]}</div>
              <div class="grid-item-{key} grid-header-{key}">{headers[2]}</div>
              <div class="grid-item-{key} grid-header-{key}">{headers[3]}</div>
              <div class="grid-item-{key} grid-header-{key}">{headers[4]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        for i, service in enumerate(services):
            st.write(
                f"""
                <div class="grid-container-{key}">
                  <div class="grid-item-{key} service-name-{key}">{service}</div>
                  <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_0"></div>
                  <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_1"></div>
                  <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_2"></div>
                  <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_3"></div>
                </div>
                """,
                unsafe_allow_html=True
            )

def display_integration_question2(question_num, question_text, key, services, headers):
    st.subheader(f'{question_num} {question_text}')
    options = ['NO', 'SI']
    selected = st.radio('Seleziona un\'opzione:', options, key=key)

    if selected == 'SI':
        st.subheader('Seleziona le caselle relative ai servizi o alle applicazioni per i quali è in funzione l’integrazione operativa')
        
        # Create grid for question
        st.write(
            f"""
            <style>
            .grid-container-{key} {{
              display: grid;
              grid-template-columns: repeat({len(headers)}, 1fr);
              gap: 1px;
              background-color: #000;
            }}
            .grid-item-{key} {{
              background-color: #fff;
              padding: 10px;
              font-size: 14px;
              text-align: center;
              border: 1px solid #ddd;
            }}
            .grid-header-{key} {{
              font-weight: bold;
              background-color: #f0f0f0;
              word-wrap: break-word;
              overflow-wrap: break-word;
              white-space: pre-wrap;
            }}
            .service-name-{key} {{
              text-align: left;
              max-width: 200px;
              word-wrap: break-word;
            }}
            </style>
            <div class="grid-container-{key}">
              <div class="grid-item-{key} grid-header-{key}">{headers[0]}</div>
              <div class="grid-item-{key} grid-header-{key}">{headers[1]}</div>
              <div class="grid-item-{key} grid-header-{key}">{headers[2]}</div>
              <div class="grid-item-{key} grid-header-{key}">{headers[3]}</div>
              <div class="grid-item-{key} grid-header-{key}">{headers[4]}</div>
              <div class="grid-item-{key} grid-header-{key}">{headers[5]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        for i, service in enumerate(services):
            st.write(
                f"""
                <div class="grid-container-{key}">
                  <div class="grid-item-{key} service-name-{key}">{service}</div>
                  <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_0"></div>
                  <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_1"></div>
                  <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_2"></div>
                  <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_3"></div>
                  <div class="grid-item-{key}"><input type="checkbox" name="service_{key}_{i}_option_4"></div>
                </div>
                """,
                unsafe_allow_html=True
            )


