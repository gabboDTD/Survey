import streamlit as st
from utils import radio_button_question, multiple_choice_question, conditional_text_input
from utils import display_data_and_process_question, display_integration_question, display_payment_reconciliation_question

def display_section_6():
    # Section 6: Servizi II (Ragioneria Tributi Patrimonio)
    st.header('SERVIZI II (Ragioneria, Tributi, Patrimonio)')

    display_data_and_process_question(
        question_num='6.1',
        question_text='Come sono gestiti dati e processi dei seguenti servizi del tuo Comune? (indica per ogni servizio una o più modalità di gestione)',
        key='6_1',
        services=[
            'Ragioneria e contabilità',
            'Tributi (maggiori e minori)',
            'Patrimonio (gestione amministrativa)'],
        headers=['Servizi',
                 'Applicazione dedicata che fa parte di una suite (applicazioni / moduli di uno stesso fornitore)', 
                 'Applicazione dedicata di singolo fornitore o sviluppata ad-hoc (applicazione specialistica)',
                 'Strumenti di office automation (elenchi, tabelle, fogli elettronici, ...)',
                 'Gestione esternalizzata o associata, totale o parziale']
    )

    # Question 6.2
    display_integration_question(
        question_num='6.2',
        question_text='I servizi o le applicazioni relative alla Ragioneria e Contabilità sono integrati con altri servizi dell’amministrazione?',
        key='6_2',
        services=[
            'Ragioneria e contabilità'
        ],
        headers=['Servizi', 
                 'Protocollo informatico', 
                 'Gestione documentale (archiviazione, fascicolazione, conservazione)', 
                 'Pubblicazioni legali e obbligatorie (albo pretorio, trasparenza)', 
                 'Anagrafiche']
    )

    # Question 6.3
    display_integration_question(
        question_num='6.3',
        question_text='I servizi o le applicazioni relative ai Tributi (maggiori e minori) sono integrati con altri servizi dell’amministrazione?',
        key='6_3',
        services=[
            'Tributi (maggiori, minori)'
        ],
        headers=['Servizi', 
                 'Protocollo informatico', 
                 'Gestione documentale (archiviazione, fascicolazione, conservazione)', 
                 'Pubblicazioni legali e obbligatorie (albo pretorio, trasparenza)', 
                 'Ragioneria e contabilità', 
                 'Anagrafiche']
    )

    # Question 6.4
    display_integration_question(
        question_num='6.4',
        question_text='I servizi o le applicazioni relative al patrimonio (gestione amministrativa) sono integrati con altri servizi dell’amministrazione?',
        key='6_4',
        services=[
            'Patrimonio (gestione amministrativa)'
        ],
        headers=['Servizi', 
                 'Protocollo informatico', 
                 'Gestione documentale (archiviazione, fascicolazione, conservazione)', 
                 'Pubblicazioni legali e obbligatorie (albo pretorio, trasparenza)', 
                 'Ragioneria e contabilità', 
                 'Anagrafiche']
    )

    # Question 6.5
    display_payment_reconciliation_question(question_num='6.5', 
                                            question_text='Per i servizi/applicazioni del tuo Comune che coinvolgono flussi di pagamenti indica se la riconciliazione dei pagamenti avviene in maniera manuale o automatica. Seleziona una o entrambe le opzioni.', 
                                            key='6_5', 
                                            services=[
                                                'Tributi',
                                                'Patrimonio (gestione amministrativa)'
                                                ]
    )
