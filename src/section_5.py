import streamlit as st
from utils import radio_button_question, multiple_choice_question
from utils import display_data_and_process_question, display_integration_question, display_integration_question2

def display_section_5():
    # Section 5: Servizi I (Protocollo Atti Segreteria generale URP)
    st.header('SERVIZI I (Protocollo, Atti, Segreteria generale, URP)')

    # Question 5.1
    display_data_and_process_question(
        question_num='5.1',
        question_text='Come sono gestiti dati e processi dei seguenti servizi del tuo Comune? (indica per ogni servizio una o più modalità di gestione)',
        key='5_1',
        services=[
        'Protocollo e gestione documentale',
        'Atti amministrativi (delibere, determinazioni dirigenziali)',
        'Segreteria (gestione organi istituzionali)',
        'URP - Ufficio Relazioni con il Pubblico'
        ],
        headers=['Servizi',
                 'Applicazione dedicata che fa parte di una suite (applicazioni / moduli di uno stesso fornitore)', 
                 'Applicazione dedicata di singolo fornitore o sviluppata ad-hoc (applicazione specialistica)',
                 'Strumenti di office automation (elenchi, tabelle, fogli elettronici, ...)',
                 'Gestione esternalizzata o associata, totale o parziale']
    )

    # Question 5.2
    display_integration_question(
        question_num='5.2',
        question_text='I servizi o le applicazioni relative agli atti amministrativi sono integrati con altri servizi dell’amministrazione?',
        key='5_2',
        services=[
            'Atti amministrativi (delibere, determinazioni dirigenziali)'
        ],
        headers=[
            'Protocollo informatico',
            'Gestione documentale (archiviazione fascicolazione conservazione)',
            'Pubblicazioni legali e obbligatorie (albo pretorio trasparenza)',
            'Ragioneria e contabilità',
            'Anagrafiche'
            ]
    )

    # Question 5.3
    st.subheader('5.3 Per i servizi/applicazioni che prevedono flussi di pagamento indica se la riconciliazione dei pagamenti ricevuti avviene in maniera manuale o automatica.')
    payment_services = ['Segreteria (contratti accesso agli atti pagamento diritti …)']
    reconciliation_options = ['Riconciliazione manuale', 'Riconciliazione automatica']

    for service in payment_services:
        st.write(f"**{service}**")
        multiple_choice_question('', reconciliation_options, key=f'5_3_{service}')
