import streamlit as st
from utils import display_data_and_process_question, display_integration_question

def display_section_9():
    # Section 9: Servizi V (Territorio, Ambiente, lavoro))
    st.header("SERVIZI V (Territorio, Ambiente, lavoro)")

    # Question 9.1
    display_data_and_process_question(
        question_num='9.1',
        question_text='Come sono gestiti dati e processi dei seguenti servizi del tuo Comune? (indica per ogni servizio una o più modalità di gestione)',
        key='9_1',
        services=['Ambiente (autorizzazioni e servizi)',
                  'Lavori e opere pubbliche',
                ],
        headers=['Servizi',
                 'Applicazione dedicata che fa parte di una suite (applicazioni / moduli di uno stesso fornitore)', 
                 'Applicazione dedicata di singolo fornitore o sviluppata ad-hoc (applicazione specialistica)',
                 'Strumenti di office automation (elenchi, tabelle, fogli elettronici, ...)',
                 'Gestione esternalizzata o associata, totale o parziale']
    )

    # Question 9.2
    display_integration_question(
        question_num='9.2',
        question_text='9.2.	I servizi o le applicazioni relative all’ambiente sono integrati con altri servizi dell’amministrazione?',
        key='9_2',
        services=['Ambiente (autorizzazioni e servizi)'],
        headers=['Servizi', 
                 'Protocollo informatico', 
                 'Gestione documentale (archiviazione, fascicolazione, conservazione)', 
                 'Pubblicazioni legali e obbligatorie (albo pretorio, trasparenza)', 
                 'Ragioneria e contabilità', 
                 'Anagrafiche']
    )
