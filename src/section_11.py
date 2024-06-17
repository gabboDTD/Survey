import streamlit as st
from utils import display_data_and_process_question, display_integration_question2

def display_section_11():
    # Section 11: Servizi VII (Polizia locale)
    st.header("SERVIZI VII (Polizia locale)")

    # Question 11.1
    display_data_and_process_question(
        question_num='11.1',
        question_text='Come sono gestiti dati e processi dei seguenti servizi del tuo Comune? (indica per ogni servizio una o più modalità di gestione)',
        key='11_1',
        services=['Polizia locale'],
        headers=['Servizi',
                 'Applicazione dedicata che fa parte di una suite (applicazioni / moduli di uno stesso fornitore)', 
                 'Applicazione dedicata di singolo fornitore o sviluppata ad-hoc (applicazione specialistica)',
                 'Strumenti di office automation (elenchi, tabelle, fogli elettronici, ...)',
                 'Gestione esternalizzata o associata, totale o parziale']
    )

    # Question 11.2
    display_integration_question2(
        question_num='11.2',
        question_text='I servizi o le applicazioni relative alla polizia locale sono integrati con altri servizi dell’amministrazione?',
        key='11_2',
        services=['Polizia locale'],
        headers=['Servizi', 'Protocollo informatico', 
                 'Gestione documentale (archiviazione, fascicolazione, conservazione)', 
                 'Pubblicazioni legali e obbligatorie (albo pretorio, trasparenza)', 
                 'Ragioneria e contabilità', 
                 'Anagrafiche']
    )
