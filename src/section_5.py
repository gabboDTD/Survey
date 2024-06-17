import streamlit as st
from utils import radio_button_question, multiple_choice_question

def display_section_5():
    # Section 5: Servizi I (Protocollo Atti Segreteria generale URP)
    st.header('SERVIZI I (Protocollo, Atti, Segreteria generale, URP)')

    st.subheader('5.1 Come sono gestiti dati e processi dei seguenti servizi del tuo Comune? (indica per ogni servizio una o più modalità di gestione)')

    services_5_1 = [
        'Protocollo e gestione documentale',
        'Atti amministrativi (delibere, determinazioni dirigenziali)',
        'Segreteria (gestione organi istituzionali)',
        'URP - Ufficio Relazioni con il Pubblico'
    ]
    management_options = [
        'Applicazione dedicata che fa parte di una suite (applicazioni / moduli di uno stesso fornitore)',
        'Applicazione dedicata di singolo fornitore o sviluppata ad-hoc (applicazione specialistica)',
        'Strumenti di office automation (elenchi tabelle fogli elettronici ...)',
        'Gestione esternalizzata o associata totale o parziale'
    ]

    # Create grid for question 5.1
    st.write(
        """
        <style>
        .grid-container-51 {
          display: grid;
          grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
          gap: 1px;
          background-color: #000;
        }
        .grid-item-51 {
          background-color: #fff;
          padding: 10px;
          font-size: 14px;
          text-align: center;
          border: 1px solid #ddd;
        }
        .grid-header-51 {
          font-weight: bold;
          background-color: #f0f0f0;
        }
        .service-name-51 {
          text-align: left;
          max-width: 200px;
          word-wrap: break-word;
        }
        </style>
        <div class="grid-container-51">
          <div class="grid-item-51 grid-header-51">Servizi</div>
          <div class="grid-item-51 grid-header-51">Applicazione dedicata che fa parte di una suite (applicazioni / moduli di uno stesso fornitore)</div>
          <div class="grid-item-51 grid-header-51">Applicazione dedicata di singolo fornitore o sviluppata ad-hoc (applicazione specialistica)</div>
          <div class="grid-item-51 grid-header-51">Strumenti di office automation (elenchi tabelle fogli elettronici ...)</div>
          <div class="grid-item-51 grid-header-51">Gestione esternalizzata o associata totale o parziale</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for i, service in enumerate(services_5_1):
        st.write(
            f"""
            <div class="grid-container-51">
              <div class="grid-item-51 service-name-51">{service}</div>
              <div class="grid-item-51"><input type="checkbox" name="service_{i}_option_0"></div>
              <div class="grid-item-51"><input type="checkbox" name="service_{i}_option_1"></div>
              <div class="grid-item-51"><input type="checkbox" name="service_{i}_option_2"></div>
              <div class="grid-item-51"><input type="checkbox" name="service_{i}_option_3"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Question 5.2
    st.subheader('5.2 I servizi o le applicazioni relative agli atti amministrativi sono integrati con altri servizi dell’amministrazione?')
    options_5_2 = ['NO', 'SI']
    selected_5_2 = radio_button_question('Seleziona un\'opzione:', options_5_2, key='5_2')

    if selected_5_2 == 'SI':
        st.subheader('Seleziona le caselle relative ai servizi o alle applicazioni per i quali è in funzione l’integrazione operativa')
        integration_options = [
            'Protocollo informatico',
            'Gestione documentale (archiviazione fascicolazione conservazione)',
            'Pubblicazioni legali e obbligatorie (albo pretorio trasparenza)',
            'Ragioneria e contabilità',
            'Anagrafiche'
        ]
        multiple_choice_question('Atti amministrativi (delibere determinazioni dirigenziali)', integration_options, key='5_2_integration')

    # Question 5.3
    st.subheader('5.3 Per i servizi/applicazioni che prevedono flussi di pagamento indica se la riconciliazione dei pagamenti ricevuti avviene in maniera manuale o automatica.')
    payment_services = ['Segreteria (contratti accesso agli atti pagamento diritti …)']
    reconciliation_options = ['Riconciliazione manuale', 'Riconciliazione automatica']

    for service in payment_services:
        st.write(f"**{service}**")
        multiple_choice_question('', reconciliation_options, key=f'5_3_{service}')
