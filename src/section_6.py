import streamlit as st
from utils import radio_button_question, multiple_choice_question, conditional_text_input

def display_section_6():
    # Section 6: Servizi II (Ragioneria Tributi Patrimonio)
    st.header('SERVIZI II (Ragioneria, Tributi, Patrimonio)')

    st.subheader('6.1 Come sono gestiti dati e processi dei seguenti servizi del tuo Comune? (indica per ogni servizio una o più modalità di gestione)')
    services_6_1 = [
        'Ragioneria e contabilità',
        'Tributi (maggiori e minori)',
        'Patrimonio (gestione amministrativa)'
    ]

    # Create grid for question 6.1
    st.write(
        """
        <style>
        .grid-container-61 {
          display: grid;
          grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
          gap: 1px;
          background-color: #000;
        }
        .grid-item-61 {
          background-color: #fff;
          padding: 10px;
          font-size: 14px;
          text-align: center;
          border: 1px solid #ddd;
        }
        .grid-header-61 {
          font-weight: bold;
          background-color: #f0f0f0;
        }
        .service-name-61 {
          text-align: left;
          max-width: 200px;
          word-wrap: break-word;
        }
        </style>
        <div class="grid-container-61">
          <div class="grid-item-61 grid-header-61">Servizi</div>
          <div class="grid-item-61 grid-header-61">Applicazione dedicata che fa parte di una suite (applicazioni / moduli di uno stesso fornitore)</div>
          <div class="grid-item-61 grid-header-61">Applicazione dedicata di singolo fornitore o sviluppata ad-hoc (applicazione specialistica)</div>
          <div class="grid-item-61 grid-header-61">Strumenti di office automation (elenchi tabelle fogli elettronici ...)</div>
          <div class="grid-item-61 grid-header-61">Gestione esternalizzata o associata totale o parziale</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for i, service in enumerate(services_6_1):
        st.write(
            f"""
            <div class="grid-container-61">
              <div class="grid-item-61 service-name-61">{service}</div>
              <div class="grid-item-61"><input type="checkbox" name="service_{i}_option_0"></div>
              <div class="grid-item-61"><input type="checkbox" name="service_{i}_option_1"></div>
              <div class="grid-item-61"><input type="checkbox" name="service_{i}_option_2"></div>
              <div class="grid-item-61"><input type="checkbox" name="service_{i}_option_3"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Question 6.2
    st.subheader('6.2 I servizi o le applicazioni relative alla Ragioneria e Contabilità sono integrati con altri servizi dell’amministrazione?')
    options_6_2 = ['NO', 'SI']
    selected_6_2 = radio_button_question('Seleziona un\'opzione:', options_6_2, key='6_2')

    if selected_6_2 == 'SI':
        st.subheader('Seleziona le caselle relative ai servizi o alle applicazioni per i quali è in funzione l’integrazione operativa')
        services_6_2_1 = [
            'Ragioneria e contabilità'
        ]

        # Create grid for question 6.2
        st.write(
            """
            <style>
            .grid-container-621 {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
            gap: 1px;
            background-color: #000;
            }
            .grid-item-621 {
            background-color: #fff;
            padding: 10px;
            font-size: 14px;
            text-align: center;
            border: 1px solid #ddd;
            }
            .grid-header-621 {
            font-weight: bold;
            background-color: #f0f0f0;
            }
            .service-name-621 {
            text-align: left;
            max-width: 200px;
            word-wrap: break-word;
            }
            </style>
            <div class="grid-container-621">
            <div class="grid-item-621 grid-header-621">Servizi</div>
            <div class="grid-item-621 grid-header-621">Protocollo informatico</div>
            <div class="grid-item-621 grid-header-621">Gestione documentale (archiviazione, fascicolazione, conservazione)</div>
            <div class="grid-item-621 grid-header-621">Pubblicazioni legali e obbligatorie (albo pretorio, trasparenza)</div>
            <div class="grid-item-621 grid-header-621">Anagrafiche</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        for i, service in enumerate(services_6_2_1):
            st.write(
                f"""
                <div class="grid-container-621">
                <div class="grid-item-621 service-name-621">{service}</div>
                <div class="grid-item-621"><input type="checkbox" name="service_{i}_option_0"></div>
                <div class="grid-item-621"><input type="checkbox" name="service_{i}_option_1"></div>
                <div class="grid-item-621"><input type="checkbox" name="service_{i}_option_2"></div>
                <div class="grid-item-621"><input type="checkbox" name="service_{i}_option_3"></div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Question 6.3
    st.subheader('6.3 I servizi o le applicazioni relative ai Tributi (maggiori e minori) sono integrati con altri servizi dell’amministrazione?')
    options_6_3 = ['NO', 'SI']
    selected_6_3 = radio_button_question('Seleziona un\'opzione:', options_6_3, key='6_3')

    if selected_6_3 == 'SI':
        st.subheader('Seleziona le caselle relative ai servizi o alle applicazioni per i quali è in funzione l’integrazione operativa')
        services_6_3_1 = [
            'Tributi (maggiori, minori)'
        ]

        # Create grid for question 6.3
        st.write(
            """
            <style>
            .grid-container-631 {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
            gap: 1px;
            background-color: #000;
            }
            .grid-item-631 {
            background-color: #fff;
            padding: 10px;
            font-size: 14px;
            text-align: center;
            border: 1px solid #ddd;
            }
            .grid-header-631 {
            font-weight: bold;
            background-color: #f0f0f0;
            }
            .service-name-631 {
            text-align: left;
            max-width: 200px;
            word-wrap: break-word;
            }
            </style>
            <div class="grid-container-631">
            <div class="grid-item-631 grid-header-631">Servizi</div>
            <div class="grid-item-631 grid-header-631">Protocollo informatico</div>
            <div class="grid-item-631 grid-header-631">Gestione documentale (archiviazione, fascicolazione, conservazione)</div>
            <div class="grid-item-631 grid-header-631">Pubblicazioni legali e obbligatorie (albo pretorio, trasparenza)</div>
            <div class="grid-item-631 grid-header-631">Ragioneria e contabilità</div>
            <div class="grid-item-631 grid-header-631">Anagrafiche</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        for i, service in enumerate(services_6_3_1):
            st.write(
                f"""
                <div class="grid-container-631">
                <div class="grid-item-631 service-name-631">{service}</div>
                <div class="grid-item-631"><input type="checkbox" name="service_{i}_option_0"></div>
                <div class="grid-item-631"><input type="checkbox" name="service_{i}_option_1"></div>
                <div class="grid-item-631"><input type="checkbox" name="service_{i}_option_2"></div>
                <div class="grid-item-631"><input type="checkbox" name="service_{i}_option_3"></div>
                <div class="grid-item-631"><input type="checkbox" name="service_{i}_option_4"></div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Question 6.4
    st.subheader('6.4 I servizi o le applicazioni relative al patrimonio (gestione amministrativa) sono integrati con altri servizi dell’amministrazione?')
    options_6_4 = ['NO', 'SI']
    selected_6_4 = radio_button_question('Seleziona un\'opzione:', options_6_4, key='6_4')

    if selected_6_4 == 'SI':
        st.subheader('Seleziona le caselle relative ai servizi o alle applicazioni per i quali è in funzione l’integrazione operativa')
        services_6_4_1 = [
            'Patrimonio (gestione amministrativa)'
        ]

        # Create grid for question 6.4
        st.write(
            """
            <style>
            .grid-container-641 {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
            gap: 1px;
            background-color: #000;
            }
            .grid-item-641 {
            background-color: #fff;
            padding: 10px;
            font-size: 14px;
            text-align: center;
            border: 1px solid #ddd;
            }
            .grid-header-641 {
            font-weight: bold;
            background-color: #f0f0f0;
            }
            .service-name-641 {
            text-align: left;
            max-width: 200px;
            word-wrap: break-word;
            }
            </style>
            <div class="grid-container-641">
            <div class="grid-item-641 grid-header-641">Servizi</div>
            <div class="grid-item-641 grid-header-641">Protocollo informatico</div>
            <div class="grid-item-641 grid-header-641">Gestione documentale (archiviazione, fascicolazione, conservazione)</div>
            <div class="grid-item-641 grid-header-641">Pubblicazioni legali e obbligatorie (albo pretorio, trasparenza)</div>
            <div class="grid-item-641 grid-header-641">Ragioneria e contabilità</div>
            <div class="grid-item-641 grid-header-641">Anagrafiche</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        for i, service in enumerate(services_6_4_1):
            st.write(
                f"""
                <div class="grid-container-641">
                <div class="grid-item-641 service-name-641">{service}</div>
                <div class="grid-item-641"><input type="checkbox" name="service_{i}_option_0"></div>
                <div class="grid-item-641"><input type="checkbox" name="service_{i}_option_1"></div>
                <div class="grid-item-641"><input type="checkbox" name="service_{i}_option_2"></div>
                <div class="grid-item-641"><input type="checkbox" name="service_{i}_option_3"></div>
                <div class="grid-item-641"><input type="checkbox" name="service_{i}_option_4"></div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.subheader('6.5 Per i servizi/applicazioni del tuo Comune che coinvolgono flussi di pagamenti indica se la riconciliazione dei pagamenti avviene in maniera manuale o automatica. Seleziona una o entrambe le opzioni.')
    services_6_5 = [
        'Tributi',
        'Patrimonio (gestione amministrativa)'
    ]

    # Create grid for question 6.5
    st.write(
        """
        <style>
        .grid-container-65 {
          display: grid;
          grid-template-columns: 0.7fr 1fr 1fr;
          gap: 0;
        }
        .grid-item-65 {
          background-color: #fff;
          padding: 10px;
          font-size: 14px;
          text-align: center;
          border: 1px solid #ddd;
          box-sizing: border-box;
        }
        .grid-header-65 {
          font-weight: bold;
          background-color: #f0f0f0;
          word-wrap: break-word;
          overflow-wrap: break-word;
          white-space: pre-wrap;
          border: 1px solid #ddd;
          box-sizing: border-box;
        }
        .service-name-65 {
          text-align: left;
          max-width: 200px;
          word-wrap: break-word;
          border: 1px solid #ddd;
          box-sizing: border-box;
        }
        </style>
        <div class="grid-container-65">
          <div class="grid-item-65 grid-header-65">Servizi che richiedono<br>pagamenti</div>
          <div class="grid-item-65 grid-header-65">Riconciliazione manuale</div>
          <div class="grid-item-65 grid-header-65">Riconciliazione automatica</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for i, service in enumerate(services_6_5):
        st.write(
            f"""
            <div class="grid-container-65">
              <div class="grid-item-65 service-name-65">{service}</div>
              <div class="grid-item-65"><input type="checkbox" name="service_{i}_option_0"></div>
              <div class="grid-item-65"><input type="checkbox" name="service_{i}_option_1"></div>
            </div>
            """,
            unsafe_allow_html=True
        )