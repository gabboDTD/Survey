import streamlit as st
from utils import multiple_choice_question, radio_button_question, number_input_question, conditional_text_input

def display_section_2():

    # Section 2: Organizzazione dell’ente e dei servizi
    st.header('2. Organizzazione dell’ente e dei servizi')

    # Question 2.1
    st.subheader('2.1 Tra le categorie riportate di seguito indica in quale rientra il tuo Comune.')
    options_2_1 = [
        'Appartenenza a un\'unione di comuni',
        'Appartenenza a una comunità montana',
        'Utilizzo di convenzione di servizi',
        'Coinvolgimento in un consorzio',
        'Il Comune opera come un\'entità amministrativa singola',
        'Altro'
    ]
    selected_2_1 = multiple_choice_question('Seleziona una o più opzioni:', options_2_1, key='2_1')
    conditional_text_input('Specificare:', 'Altro' in selected_2_1, key='2_1_other')

    # Question 2.2
    st.subheader('2.2 Il tuo Comune è socio di una società pubblica che si occupa di fornire servizi ICT?')
    options_2_2 = [
        'SI, il mio Comune possiede una quota societaria di una società di servizi con competenze ICT',
        'SI, il mio Comune è socio unico di una società di servizi con competenze ICT',
        'NO, il mio Comune non gestisce una propria società di servizi con competenze ICT'
    ]
    selected_2_2 = radio_button_question('Seleziona un\'opzione:', options_2_2, key='2_2')

    # Question 2.3
    st.subheader('2.3 Il tuo Comune come gestisce i servizi ICT?')
    options_2_3 = [
        'Il Comune gestisce autonomamente in tutto o in parte i sistemi ICT',
        'Il Comune si avvale di uno o più fornitori esterni per i servizi ICT',
        'Il Comune ha una propria società in-house che gestisce i servizi ICT',
        'Non sono disponibili informazioni sul modello di gestione ICT del Comune',
        'Il Comune partecipa a una gestione ICT associata con altri enti pubblici'
    ]
    selected_2_3 = multiple_choice_question('Seleziona una o più opzioni:', options_2_3, key='2_3')

    # Question 2.4
    st.subheader('2.4 In merito alla gestione dei servizi ICT indica il numero di risorse IT che sono previste in pianta organica nel tuo Comune.')
    num_resources_planned = number_input_question('Numero di risorse IT previste:', key='2_4')

    # Conditional Questions 2.4.1 to 2.4.3 based on previous answers
    if num_resources_planned > 0:
        num_resources_operational = number_input_question('Numero di risorse IT effettivamente operativo:', key='2_4_1')
        if num_resources_planned != num_resources_operational:
            reasons_for_difference = multiple_choice_question(
                'Quali sono le ragioni principali che causano una differenza tra il personale IT previsto e quello realmente disponibile?',
                ['Mancanza di fondi', 'Difficoltà nel reperimento di personale qualificato', 'Vincoli normativi', 'Altri motivi'], key='2_4_2'
            )
            conditional_text_input('Specificare:', 'Altri motivi' in reasons_for_difference, key='2_4_2_other')

        resource_types = multiple_choice_question(
            'In merito al personale IT indica la tipologia delle risorse selezionando una o più opzioni.',
            ['Interno all’ente', 'Condiviso con altri Enti', 'Esterno'], key='2_4_3'
        )

    # Question 2.5
    st.subheader('2.5 In merito alla figura del responsabile dei sistemi informativi indica la tipologia selezionando una o più opzioni:')
    options_2_5 = [
        'Interno all’ente',
        'Condiviso con altri Enti (Unioni, Comunità montane, Convenzioni, Consorzi)',
        'Altro (specificare)'
    ]
    selected_2_5 = multiple_choice_question('Seleziona una o più opzioni:', options_2_5, key='2_5')
    conditional_text_input('Specificare:', 'Altro (specificare)' in selected_2_5, key='2_5_other')

    # Question 2.6
    st.subheader('2.6 In merito alla figura del responsabile dei sistemi informativi indica se è dedicato esclusivamente a quella funzione o svolge anche altre funzioni (non dedicato)')
    options_2_6 = [
        'Dedicato',
        'Non dedicato'
    ]
    selected_2_6 = radio_button_question('Seleziona un\'opzione:', options_2_6, key='2_6')

    # Question 2.7
    st.subheader('2.7 In merito alle competenze del responsabile dei sistemi informativi indica la tipologia selezionando una o più opzioni:')
    options_2_7 = [
        'esclusivamente amministrativo',
        'esclusivamente tecnologico',
        'organizzativo e strategico'
    ]
    selected_2_7 = multiple_choice_question('Seleziona una o più opzioni:', options_2_7, key='2_7')

    # Question 2.8
    st.subheader('2.8 Il tuo Comune ha nominato come Responsabile per la Transizione Digitale (RTD) una figura:')
    options_2_8 = [
        'Interna dedicato',
        'Interna ma che svolge anche il ruolo di Responsabile dell’Information Technology (IT/ITC)',
        'Interna ma che svolge anche un ruolo di Responsabile apicale di altro servizio',
        'In condivisione con altri Comuni',
        'In fase di nomina',
        'Altro (specificare)'
    ]
    selected_2_8 = radio_button_question('Seleziona un\'opzione:', options_2_8, key='2_8')
    conditional_text_input('Specificare:', 'Altro (specificare)' in selected_2_8, key='2_8_other')

    # Question 2.9
    st.subheader('2.9 In merito al Responsabile per la Protezione dati (DPO) il tuo Comune ha nominato:')
    options_2_9 = [
        'Responsabile per la Protezione dati (DPO) interno',
        'Responsabile per la Protezione dati (DPO) esterno',
        'Responsabile per la Protezione dati (DPO) In condivisione con altri Comuni',
        'Responsabile per la Protezione dati (DPO) in fase di nomina',
        'Altro (specificare)'
    ]
    selected_2_9 = radio_button_question('Seleziona un\'opzione:', options_2_9, key='2_9')
    conditional_text_input('Specificare:', 'Altro (specificare)' in selected_2_9, key='2_9_other')

    # Question 2.10
    st.subheader('2.10 In merito al Responsabile della Gestione Informatica dei Documenti e del Protocollo Informatico il tuo Comune ha nominato:')
    options_2_10 = [
        'Responsabile della Gestione Informatica dei Documenti e del Protocollo Informatico con funzioni proprie e autonome',
        'Responsabile della Gestione Informatica dei Documenti e del Protocollo Informatico In condivisione con altri Comuni',
        'Responsabile della Gestione Informatica dei Documenti e del Protocollo Informatico in fase di nomina',
        'Altro (specificare)'
    ]
    selected_2_10 = radio_button_question('Seleziona un\'opzione:', options_2_10, key='2_10')
    conditional_text_input('Specificare:', 'Altro (specificare)' in selected_2_10, key='2_10_other')

    # Question 2.11
    st.subheader('2.11 In merito al Responsabile della Conservazione interno il tuo Comune ha nominato:')
    options_2_11 = [
        'Responsabile della Conservazione interno autonomo dalla Gestione Documentale',
        'Responsabile della Conservazione che svolge anche il ruolo di Responsabile della Gestione Informatica dei Documenti e del Protocollo Informatico',
        'Responsabile della Conservazione in condivisione con altri Comuni',
        'Responsabile della Conservazione in fase di nomina',
        'Altro (specificare)'
    ]
    selected_2_11 = radio_button_question('Seleziona un\'opzione:', options_2_11, key='2_11')
    conditional_text_input('Specificare:', 'Altro (specificare)' in selected_2_11, key='2_11_other')

    # Question 2.12
    st.subheader('2.12 In merito al Responsabile della sicurezza informatica il tuo Comune ha nominato:')
    options_2_12 = [
        'Responsabile della sicurezza informatica (cybersecurity) interno distinto dal Responsabile IT',
        'Responsabile della sicurezza informatica (cybersecurity) In condivisione con altri Comuni',
        'Responsabile della sicurezza informatica in fase di nomina',
        'Altro (specificare)'
    ]
    selected_2_12 = radio_button_question('Seleziona un\'opzione:', options_2_12, key='2_12')
    conditional_text_input('Specificare:', 'Altro (specificare)' in selected_2_12, key='2_12_other')

    # Question 2.13 as a Grid
    st.subheader('2.13 In merito alla formazione sulle competenze digitali del personale del tuo Comune indica il livello di supporto necessario per ciascuna delle voci seguenti.')

    competencies = ['Utilizzo di software specifici', 'Gestione dei dati digitali', 'Comunicazione su canali digitale', 'Sicurezza informatica', 'Programmazione', 'Utilizzo di piattaforme collaborative', 'Analisi dei dati']
    support_levels = ['Nessun supporto', 'Supporto minimo', 'Supporto moderato', 'Supporto significativo']

    # Create grid for question 2.13
    st.write(
        """
        <style>
        .grid-container-213 {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
        gap: 1px;
        background-color: #000;
        }
        .grid-item-213 {
        background-color: #fff;
        padding: 10px;
        font-size: 14px;
        text-align: center;
        border: 1px solid #ddd;
        }
        .grid-header-213 {
        font-weight: bold;
        background-color: #f0f0f0;
        }
        .competenze-213 {
        text-align: left;
        max-width: 200px;
        word-wrap: break-word;
        }
        </style>
        <div class="grid-container-213">
        <div class="grid-item-213 grid-header-213">Competenze</div>
        <div class="grid-item-213 grid-header-213">Nessun supporto</div>
        <div class="grid-item-213 grid-header-213">Supporto minimo</div>
        <div class="grid-item-213 grid-header-213">Supporto moderato</div>
        <div class="grid-item-213 grid-header-213">Supporto significativo</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for i, competency in enumerate(competencies):
        st.write(
            f"""
            <div class="grid-container-213">
            <div class="grid-item-213 competenze-213">{competency}</div>
            <div class="grid-item-213"><input type="radio" name="competency_{i}" value="Nessun supporto"></div>
            <div class="grid-item-213"><input type="radio" name="competency_{i}" value="Supporto minimo"></div>
            <div class="grid-item-213"><input type="radio" name="competency_{i}" value="Supporto moderato"></div>
            <div class="grid-item-213"><input type="radio" name="competency_{i}" value="Supporto significativo"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Question 2.14 as a Grid
    st.subheader('2.14 Nell’ambito della formazione ICT che il tuo Comune offre ai dipendenti indica per ciascuna delle voci seguenti se il corso è obbligatorio, opzionale, o non previsto.')

    training_topics = ['Corso base (ad esempio strumenti MSFT Office, fogli di calcolo, accesso al cloud ecc.)', 'Corsi gestione dei dati (es. dati aperti)', 'Corsi di gestione di infrastrutture complesse di servizi digitali', 'Corsi su piattaforme specializzate (ad esempio GIS, e-procurement ecc.)', 'Altro (specificare)']
    training_options = ['Obbligatorio', 'Opzionale', 'Non previsto']

    # Create grid for question 2.14
    st.write(
        """
        <style>
        .grid-container-214 {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 1px;
        background-color: #000;
        }
        .grid-item-214 {
        background-color: #fff;
        padding: 10px;
        font-size: 14px;
        text-align: center;
        border: 1px solid #ddd;
        }
        .grid-header-214 {
        font-weight: bold;
        background-color: #f0f0f0;
        }
        .competenze-214 {
        text-align: left;
        max-width: 200px;
        word-wrap: break-word;
        }
        </style>
        <div class="grid-container-214">
        <div class="grid-item-214 grid-header-214">Temi di formazione</div>
        <div class="grid-item-214 grid-header-214">Obbligatorio</div>
        <div class="grid-item-214 grid-header-214">Opzionale</div>
        <div class="grid-item-214 grid-header-214">Non previsto</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for i, topic in enumerate(training_topics):
        st.write(
            f"""
            <div class="grid-container-214">
            <div class="grid-item-214 competenze-214">{topic}</div>
            <div class="grid-item-214"><input type="radio" name="topic_{i}" value="Obbligatorio"></div>
            <div class="grid-item-214"><input type="radio" name="topic_{i}" value="Opzionale"></div>
            <div class="grid-item-214"><input type="radio" name="topic_{i}" value="Non previsto"></div>
            </div>
            """,
            unsafe_allow_html=True
        )