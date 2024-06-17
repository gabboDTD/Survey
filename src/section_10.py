import streamlit as st
from utils import display_data_and_process_question, display_integration_question2

def display_section_10():
    # Section 10: Servizi VI (Demografici, Personale, Servizi cimiteriali)
    st.header("SERVIZI VI (Demografici, Personale, Servizi cimiteriali)")

    # Question 10.1
    display_data_and_process_question(
        question_num='10.1',
        question_text='Come sono gestiti dati e processi dei seguenti servizi del tuo Comune? (indica per ogni servizio una o più modalità di gestione)',
        key='10_1',
        services=['Demografici (anagrafe, stato civile, elettorale, leva, statistica)',
                  'Personale (gestione economica e giuridica)',
                  'Servizi cimiteriali'],
        headers=['Servizi',
                 'Applicazione dedicata che fa parte di una suite (applicazioni / moduli di uno stesso fornitore)', 
                 'Applicazione dedicata di singolo fornitore o sviluppata ad-hoc (applicazione specialistica)',
                 'Strumenti di office automation (elenchi, tabelle, fogli elettronici, ...)',
                 'Gestione esternalizzata o associata, totale o parziale']
    )

    # Question 10.2
    display_integration_question2(
        question_num='10.2',
        question_text='I servizi o le applicazioni relative ai servizi cimiteriali sono integrati con altri servizi dell’amministrazione?',
        key='10_2',
        services=['Servizi cimiteriali'],
        headers=['Servizi', 
                 'Protocollo informatico', 
                 'Gestione documentale (archiviazione, fascicolazione, conservazione)', 
                 'Pubblicazioni legali e obbligatorie (albo pretorio, trasparenza)', 
                 'Ragioneria e contabilità', 
                 'Anagrafiche']
    )
