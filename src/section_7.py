import streamlit as st
from utils import display_data_and_process_question, display_integration_question

def display_section_7():
    # Section 7: Servizi III (Servizi sociali Servizi scolastici)
    st.header("SERVIZI III (Servizi sociali Servizi scolastici)")

    # Question 7.1
    display_data_and_process_question(
        question_num='7.1',
        question_text='Come sono gestiti dati e processi dei seguenti servizi del tuo Comune? (indica per ogni servizio una o più modalità di gestione)',
        key='7_1',
        services=['Servizi sociali e disabilità (welfare)','Servizi scolastici'],
        headers=['Servizi',
                 'Applicazione dedicata che fa parte di una suite (applicazioni / moduli di uno stesso fornitore)', 
                'Applicazione dedicata di singolo fornitore o sviluppata ad-hoc (applicazione specialistica)',
                'Strumenti di office automation (elenchi, tabelle, fogli elettronici, ...)',
                'Gestione esternalizzata o associata, totale o parziale']
    )

    # Question 7.2
    display_integration_question(
        question_num='7.2',
        question_text='I servizi o le applicazioni relative ai servizi sociali e disabilità sono integrati con altri servizi dell’amministrazione?',
        key='7_2',
        services=['Servizi sociali e disabilità (welfare)'],
        headers=['Servizi', 
                 'Protocollo informatico', 
                 'Gestione documentale (archiviazione, fascicolazione, conservazione)', 
                 'Pubblicazioni legali e obbligatorie (albo pretorio, trasparenza)', 
                 'Anagrafiche']
    )
