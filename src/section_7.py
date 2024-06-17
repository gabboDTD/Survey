import streamlit as st

def display_section_7():
    # Section 7: Servizi III (Servizi sociali Servizi scolastici)
    st.header("SERVIZI III (Servizi sociali Servizi scolastici)")

    st.subheader('2.13 In merito alla formazione sulle competenze digitali del personale del tuo Comune indica il livello di supporto necessario per ciascuna delle voci seguenti.')
    services_7_1 = ['Servizi sociali e disabilità (welfare)', 
                    'Servizi scolastici'
    ]

    # Create grid for question 7.1
    st.write(
        """
        <style>
        .grid-container-71 {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
        gap: 1px;
        background-color: #000;
        }
        .grid-item-71 {
        background-color: #fff;
        padding: 10px;
        font-size: 14px;
        text-align: center;
        border: 1px solid #ddd;
        }
        .grid-header-71 {
        font-weight: bold;
        background-color: #f0f0f0;
        }
        .competenze-71 {
        text-align: left;
        max-width: 200px;
        word-wrap: break-word;
        }
        </style>
        <div class="grid-container-71">
        <div class="grid-item-71 grid-header-71">Servizi</div>
        <div class="grid-item-71 grid-header-71">Applicazione dedicata che fa parte di una suite (applicazioni / moduli di uno stesso fornitore)</div>
        <div class="grid-item-71 grid-header-71">Applicazione dedicata di singolo fornitore o sviluppata ad-hoc (applicazione specialistica)</div>
        <div class="grid-item-71 grid-header-71">Strumenti di office automation (elenchi tabelle fogli elettronici ...)</div>
        <div class="grid-item-71 grid-header-71">Gestione esternalizzata o associata totale o parziale</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for i, service in enumerate(services_7_1):
        st.write(
            f"""
            <div class="grid-container-71">
            <div class="grid-item-71 service-name-71">{service}</div>
            <div class="grid-item-71"><input type="checkbox" name="service_{i}_option_0"></div>
            <div class="grid-item-71"><input type="checkbox" name="service_{i}_option_1"></div>
            <div class="grid-item-71"><input type="checkbox" name="service_{i}_option_2"></div>
            <div class="grid-item-71"><input type="checkbox" name="service_{i}_option_3"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

        
        
        
        


    # # 7.2 Integration with other administration services
    # st.write("7.2 I servizi o le applicazioni relative ai servizi sociali e disabilità sono integrati con altri servizi dell’amministrazione?")
    # integrated_with_other_services = st.radio("Se sì, seleziona i servizi o le applicazioni per i quali è in funzione l’integrazione operativa", options=["NO", "SI"], key="integration_services_sociali")
    # integration_options = [
    #     "Protocollo informatico",
    #     "Gestione documentale (archiviazione fascicolazione conservazione)",
    #     "Pubblicazioni legali e obbligatorie (albo pretorio trasparenza)",
    #     "Ragioneria e contabilità",
    #     "Anagrafiche"
    # ]
    # if integrated_with_other_services == "SI":
    #     for option in integration_options:
    #         st.checkbox(option, key=f"integration_sociali_{option}")

    # st.write("7.3 I servizi o le applicazioni relative ai servizi scolastici sono integrati con altri servizi dell’amministrazione?")
    # integrated_with_other_services_scolastici = st.radio("Se sì, seleziona i servizi o le applicazioni per i quali è in funzione l’integrazione operativa", options=["NO", "SI"], key="integration_services_scolastici")
    # if integrated_with_other_services_scolastici == "SI":
    #     for option in integration_options:
    #         st.checkbox(option, key=f"integration_scolastici_{option}")

    # # 7.4 Integration with external services
    # external_services_options = [
    #     "Regione",
    #     "Anagrafe ANPR",
    #     "INPS (es.: ISEE SIUSS)",
    #     "Agenzia delle entrate",
    #     "Altri servizi esterni"
    # ]

    # st.write("7.4 I servizi o le applicazioni relative ai servizi sociali e disabilità sono integrati con altri servizi esterni (INPS ANPR etc.)?")
    # integrated_with_external_services_sociali = st.radio("Se sì, seleziona i servizi o le applicazioni per i quali è in funzione l’integrazione operativa", options=["NO", "SI"], key="integration_external_services_sociali")
    # if integrated_with_external_services_sociali == "SI":
    #     for option in external_services_options:
    #         st.checkbox(option, key=f"external_integration_sociali_{option}")

    # st.write("7.5 I servizi o le applicazioni relative ai servizi scolastici sono integrati con altri servizi esterni (INPS ANPR etc.)?")
    # integrated_with_external_services_scolastici = st.radio("Se sì, seleziona i servizi o le applicazioni per i quali è in funzione l’integrazione operativa", options=["NO", "SI"], key="integration_external_services_scolastici")
    # if integrated_with_external_services_scolastici == "SI":
    #     for option in external_services_options:
    #         st.checkbox(option, key=f"external_integration_scolastici_{option}")

    # # 7.6 Payment reconciliation
    # st.write("7.6 Per i servizi/applicazioni del tuo Comune che coinvolgono flussi di pagamenti indica se la riconciliazione dei pagamenti avviene in maniera manuale o automatica. (seleziona una o entrambe le opzioni)")
    # payment_services = [
    #     "Servizi sociali e disabilità (welfare)",
    #     "Servizi scolastici (asili pre/post scuola ...)",
    #     "Servizi scolastici (mensa trasporti…)"
    # ]

    # for service in payment_services:
    #     st.write(f"**{service}**")
    #     st.checkbox("Riconciliazione manuale", key=f"manual_reconciliation_{service}")
    #     st.checkbox("Riconciliazione automatica", key=f"automatic_reconciliation_{service}")

    # # 7.7 Degree of digitalization
    # st.write("7.7 In relazione al grado di digitalizzazione dei servizi forniti dal tuo Comune indica una tra le opzioni proposte per i seguenti ambiti di servizio.")
    # digitalization_options = [
    #     "La maggior parte dei servizi erogati non è digitale",
    #     "La maggior parte dei servizi è digitale solo nel back-office",
    #     "La maggior parte dei servizi è digitalizzata solo nel front-office (prenotazioni pagamenti etc.)",
    #     "La maggior parte dei servizi forniti è completamente erogata in modo digitale (front-office e back-office)"
    # ]

    # for service in services_sociali:
    #     st.write(f"**{service}**")
    #     st.radio("", options=digitalization_options, key=f"digitalization_{service}")