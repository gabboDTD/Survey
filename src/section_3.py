import streamlit as st
from utils import radio_button_question, multiple_choice_question, number_input_question, conditional_text_input

def display_section_3():
    # Section 3: Infrastruttura ICT
    st.header('3. Infrastruttura ICT')

    # Question 3.1
    st.subheader('3.1 Allo stato attuale nel tuo Comune sono operativi server fisici per la gestione e l’utilizzo di applicazioni e dati?')
    options_3_1 = [
        'SI esistono server attivi all’interno del Comune per la gestione di applicazioni e dati',
        'NO non sono più previsti server installati presso il Comune poiché è stata completata la migrazione al cloud',
        'NO non è più attivo un server per la gestione di applicazioni e dati ma sono attivi alcuni sistemi per la gestione e la protezione della rete e degli accessi',
        'NO le applicazioni sono state già migrate sul cloud ma il file server con documenti dati immagini ecc. sono archiviati in locale in cartelle condivise.'
    ]
    selected_3_1 = radio_button_question('Seleziona un\'opzione:', options_3_1, key='3_1')

    # Question 3.2
    st.subheader('3.2 In quale percentuale sono stati dismessi i server prima presenti nel data center del tuo Comune a seguito della migrazione al cloud di applicazioni e dati?')
    options_3_2 = [
        'Non è stato dismesso ancora nessun server (0%)',
        'Meno del 25%',
        'Dal 25% al 50%',
        'Dal 50% al 75%',
        'Più del 75%'
    ]
    selected_3_2 = radio_button_question('Seleziona un\'opzione:', options_3_2, key='3_2')

    if selected_3_2 in ['Non è stato dismesso ancora nessun server (0%)', 'Meno del 25%']:
        st.subheader('Qual è l\'età approssimativa dei server fisici in uso nel data center locale (on-premise) del tuo Comune?')
        options_3_2_1 = [
            'Meno di 5 anni (tutti o alcuni)',
            'Da 5 a 10 anni (tutti o alcuni)',
            'Più di 10 anni (alcuni)',
            'Non sono disponibili informazioni nel dettaglio'
        ]
        selected_3_2_1 = radio_button_question('Seleziona un\'opzione:', options_3_2_1, key='3_2_1')

    # Question 3.3
    st.subheader('3.3 Se il tuo Comune ancora possiede un server locale quali tipi di dati sono archiviati sul file server locale del tuo Comune in cartelle condivise o personali? Seleziona una o più opzioni.')
    options_3_3 = [
        'Documenti amministrativi di testo (doc, PDF, etc.)',
        'File multimediali (immagini, video, audio)',
        'Progetti e documenti tecnici in formato grafico',
        'Dati gestiti con strumenti di office automation (fogli di calcolo, etc.)',
        'Documenti amministrativi originali sottoscritti digitalmente',
        'Presentazioni e materiale di informazione e comunicazione',
        'Archivio di posta elettronica (POP3)',
        'Altro'
    ]
    selected_3_3 = multiple_choice_question('Seleziona una o più opzioni:', options_3_3, key='3_3')
    if 'Altro' in selected_3_3:
        st.text_input('Specificare:', key='3_3_other')

    # Question 3.4
    st.subheader('3.4 Indica la percentuale di dispositivi (computer desktop, notebook, etc.) in uso maggiore di cinque anni:')
    options_3_4 = ['< 20%', '20% - 50%', '>50%']
    selected_3_4 = radio_button_question('Seleziona un\'opzione:', options_3_4, key='3_4')

    # Question 3.5
    st.subheader('3.5 In merito alle postazioni di lavoro indica approssimativamente la percentuale dei sistemi operativi installati sui dispositivi in uso nel tuo Comune (indicare 0% se nessuno):')
    st.number_input('Windows 11 (%):', min_value=0, max_value=100, key='3_5_windows11')
    st.number_input('Windows 10 (%):', min_value=0, max_value=100, key='3_5_windows10')
    st.number_input('Versioni Windows precedenti (%):', min_value=0, max_value=100, key='3_5_windows_old')
    st.number_input('MacOS (%):', min_value=0, max_value=100, key='3_5_macos')
    st.number_input('Linux (%):', min_value=0, max_value=100, key='3_5_linux')

    # Question 3.6
    st.subheader('3.6 Nel tuo Comune è concesso a dipendenti o amministratori l’accesso ad applicazioni e dati interni da dispositivi mobili quali notebook, tablet e smartphone?')
    options_3_6 = [
        'SI, ma solo da dispositivi forniti dal Comune per accedere all’area interna',
        'SI, anche da dispositivi propri per accedere ad applicazioni e dati del proprio ufficio/servizio',
        'NO, non è possibile accedere da dispositivi mobili ad applicazioni o a dati interni'
    ]
    selected_3_6 = radio_button_question('Seleziona un\'opzione:', options_3_6, key='3_6')

    # Question 3.7
    st.subheader('3.7 Quale tipo di connettività è attualmente in uso nel tuo Comune?')
    options_3_7 = ['Fibra ottica', 'DSL / ADSL', 'Rete mobile (4G/5G)', 'Satellite', 'Altro']
    selected_3_7 = multiple_choice_question('Seleziona una o più opzioni:', options_3_7, key='3_7')
    if 'Altro' in selected_3_7:
        st.text_input('Specificare:', key='3_7_other')

    # Question 3.8
    st.subheader('3.8 In relazione alla velocità media di download e upload della connessione internet utilizzata nel tuo Comune seleziona un’opzione tra quelle proposte.')
    st.write('Velocità di download:')
    download_speed = ['Inferiore a 10 Mbps', '10-50 Mbps', '51-100 Mbps', 'Oltre 100 Mbps', 'Non disponibile']
    selected_download_speed = radio_button_question('Seleziona un\'opzione:', download_speed, key='3_8_download')

    st.write('Velocità di upload:')
    upload_speed = ['Inferiore a 10 Mbps', '10-50 Mbps', '51-100 Mbps', 'Oltre 100 Mbps', 'Non disponibile']
    selected_upload_speed = radio_button_question('Seleziona un\'opzione:', upload_speed, key='3_8_upload')

    # Question 3.9
    st.subheader('3.9 Sono stati riscontrati problemi di connettività nell\'utilizzo di applicazioni disponibili in cloud?')
    options_3_9 = ['NO, nessun problema riscontrato', 'SI']
    selected_3_9 = radio_button_question('Seleziona un\'opzione:', options_3_9, key='3_9')

    if selected_3_9 == 'SI':
        st.write('Indica quali applicazioni:')
        issues = [
            'SI nell’utilizzo di applicazioni di office automation',
            'SI nell’utilizzo della posta elettronica',
            'SI nell’utilizzo di applicazioni per la gestione dei servizi del Comune (es software per la gestione della ragioneria, software per la gestione del protocollo, etc.)',
            'SI nell’utilizzo di servizi erogati da altri enti (ANPR, INPS, REGIS)',
            'SI altro'
        ]
        selected_issues = multiple_choice_question('Seleziona una o più opzioni:', issues, key='3_9_issues')
        if 'SI altro' in selected_issues:
            st.text_input('Specificare:', key='3_9_issues_other')

    # Question 3.10
    st.subheader('3.10 Tra le ragioni principali proposte di seguito per cui le applicazioni in cloud funzionano lentamente indica il livello di probabilità con cui potrebbero verificarsi.')
    st.write(
        """
        <style>
        .grid-container-310 {
          display: grid;
          grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
          gap: 1px;
          background-color: #000;
        }
        .grid-item-310 {
          background-color: #fff;
          padding: 10px;
          font-size: 14px;
          text-align: center;
          border: 1px solid #ddd;
        }
        .grid-header-310 {
          font-weight: bold;
          background-color: #f0f0f0;
        }
        .motivation-310 {
          text-align: left;
          max-width: 200px;
          word-wrap: break-word;
        }
        </style>
        <div class="grid-container-310">
          <div class="grid-item-310 grid-header-310">Motivazioni</div>
          <div class="grid-item-310 grid-header-310">Per niente probabile</div>
          <div class="grid-item-310 grid-header-310">Poco probabile</div>
          <div class="grid-item-310 grid-header-310">Probabile</div>
          <div class="grid-item-310 grid-header-310">Molto probabile</div>
          <div class="grid-item-310 grid-header-310">Sicuramente</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    motivations = [
        'Problemi di congestione di rete durante determinati orari',
        'Limitazioni tecniche o problemi di configurazione della rete',
        'Problemi con il fornitore del servizio cloud',
        'Mancanza di aggiornamenti o manutenzione della connessione internet',
        'Ostacoli geografici o topografici',
        'Limitazioni di budget e priorità organizzative',
        'Altro (specificare)'
    ]

    for i, motivation in enumerate(motivations):
        st.write(
            f"""
            <div class="grid-container-310">
              <div class="grid-item-310 motivation-310">{motivation}</div>
              <div class="grid-item-310"><input type="radio" name="motivation_{i}" value="Per niente probabile"></div>
              <div class="grid-item-310"><input type="radio" name="motivation_{i}" value="Poco probabile"></div>
              <div class="grid-item-310"><input type="radio" name="motivation_{i}" value="Probabile"></div>
              <div class="grid-item-310"><input type="radio" name="motivation_{i}" value="Molto probabile"></div>
              <div class="grid-item-310"><input type="radio" name="motivation_{i}" value="Sicuramente"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Question 3.11
    st.subheader('3.11 Nel tuo Comune è attiva una di linea di backup per garantire la continuità operativa nella connettività?')
    options_3_11 = ['NO', 'Non sono disponibili informazioni', 'SI']
    selected_3_11 = radio_button_question('Seleziona un\'opzione:', options_3_11, key='3_11')

    if selected_3_11 == 'SI':
        backup_options = [
            'Linea di backup via fibra ottica',
            'Linea di backup via DSL',
            'Linea di backup wireless (es. 4G/5G)'
        ]
        multiple_choice_question('Seleziona una o più opzioni:', backup_options, key='3_11_backup')

    # Question 3.12
    st.subheader('3.12 Per le seguenti categorie di servizi ICT indica se la modalità di erogazione è tramite personale interno o affidamento esterno.')
    st.write(
        """
        <style>
        .grid-container-312 {
          display: grid;
          grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
          gap: 1px;
          background-color: #000;
        }
        .grid-item-312 {
          background-color: #fff;
          padding: 10px;
          font-size: 14px;
          text-align: center;
          border: 1px solid #ddd;
        }
        .grid-header-312 {
          font-weight: bold;
          background-color: #f0f0f0;
        }
        .service-category-312 {
          text-align: left;
          max-width: 200px;
          word-wrap: break-word;
        }
        </style>
        <div class="grid-container-312">
          <div class="grid-item-312 grid-header-312">Categoria di Servizio</div>
          <div class="grid-item-312 grid-header-312">Interni</div>
          <div class="grid-item-312 grid-header-312">Esterni</div>
          <div class="grid-item-312 grid-header-312">Entrambi</div>
          <div class="grid-item-312 grid-header-312">Nessuno</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    service_categories = [
        'Servizi di assistenza sistemistica',
        'Servizi di assistenza al dipendente (hardware e software)',
        'Servizi di cybersicurezza'
    ]

    for i, category in enumerate(service_categories):
        st.write(
            f"""
            <div class="grid-container-312">
              <div class="grid-item-312 service-category-312">{category}</div>
              <div class="grid-item-312"><input type="radio" name="category_{i}" value="Interni"></div>
              <div class="grid-item-312"><input type="radio" name="category_{i}" value="Esterni"></div>
              <div class="grid-item-312"><input type="radio" name="category_{i}" value="Entrambi"></div>
              <div class="grid-item-312"><input type="radio" name="category_{i}" value="Nessuno"></div>
            </div>
            """,
            unsafe_allow_html=True
        )
