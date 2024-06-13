import streamlit as st
from utils import radio_button_question, multiple_choice_question, conditional_text_input

def display_section_4():
    # Section 4: Sicurezza
    st.header('4. Sicurezza')

    # Question 4.1
    st.subheader('4.1 Come è gestito il backup dei dati e dei sistemi nel tuo Comune?')
    options_4_1 = [
        'Tramite backup locale',
        'Tramite backup in cloud',
        'Utilizzando entrambe le modalità: locale e in cloud'
    ]
    selected_4_1 = radio_button_question('Seleziona un\'opzione:', options_4_1, key='4_1')

    # Question 4.2
    st.subheader('4.2 Quali tra le seguenti soluzioni e procedure sono attualmente implementate per proteggere e salvaguardare i dati, le applicazioni e i sistemi nel tuo Comune?')
    options_4_2 = [
        'Monitoraggio e verifica dei backup',
        'Crittografia dei dati sensibili in transito e a riposo',
        'Monitoraggio costante delle attività dei sistemi (log di sistema)',
        'Formazione periodica per i dipendenti del Comune sull\'importanza della sicurezza informatica e sulle migliori pratiche per proteggere i dati',
        'Audit e vulnerability assessment (valutazioni indipendenti) regolari dei sistemi e delle procedure di sicurezza per valutare la conformità e l\'efficacia',
        'Utilizzo di password manager',
        'Sistema di autenticazione a più fattori (ad esempio utilizzo di password e codici OTP)',
        'Altro'
    ]
    selected_4_2 = multiple_choice_question('Seleziona una o più opzioni:', options_4_2, key='4_2')
    if 'Altro' in selected_4_2:
        st.text_input('Specificare:', key='4_2_other')

    # Question 4.3
    st.subheader('4.3 In merito al tema della cyber sicurezza indica la quantità di attacchi informatici per ogni tipologia di seguito elencata che il tuo Comune ha subito dall’inizio del 2023.')
    st.write(
        """
        <style>
        .grid-container-43 {
          display: grid;
          grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
          gap: 1px;
          background-color: #000;
        }
        .grid-item-43 {
          background-color: #fff;
          padding: 10px;
          font-size: 14px;
          text-align: center;
          border: 1px solid #ddd;
        }
        .grid-header-43 {
          font-weight: bold;
          background-color: #f0f0f0;
        }
        .attack-type-43 {
          text-align: left;
          max-width: 200px;
          word-wrap: break-word;
        }
        </style>
        <div class="grid-container-43">
          <div class="grid-item-43 grid-header-43">Tipologia di attacco</div>
          <div class="grid-item-43 grid-header-43">Nessun attacco (0)</div>
          <div class="grid-item-43 grid-header-43">Pochi attacchi (1-5)</div>
          <div class="grid-item-43 grid-header-43">Alcuni attacchi (6-20)</div>
          <div class="grid-item-43 grid-header-43">Numerosi attacchi (oltre 20)</div>
          <div class="grid-item-43 grid-header-43">Dato non disponibile</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    attack_types = [
        'Malware',
        'Phishing',
        'Ransomware',
        'Attacchi DDoS',
        'Accesso non autorizzato ai sistemi',
        'Violazioni dei dati sensibili',
        'Altri tipi di attacchi informatici'
    ]

    for i, attack in enumerate(attack_types):
        st.write(
            f"""
            <div class="grid-container-43">
              <div class="grid-item-43 attack-type-43">{attack}</div>
              <div class="grid-item-43"><input type="radio" name="attack_{i}" value="Nessun attacco (0)"></div>
              <div class="grid-item-43"><input type="radio" name="attack_{i}" value="Pochi attacchi (1-5)"></div>
              <div class="grid-item-43"><input type="radio" name="attack_{i}" value="Alcuni attacchi (6-20)"></div>
              <div class="grid-item-43"><input type="radio" name="attack_{i}" value="Numerosi attacchi (oltre 20)"></div>
              <div class="grid-item-43"><input type="radio" name="attack_{i}" value="Dato non disponibile"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Question 4.4
    st.subheader('4.4 Quando si verificano incidenti dovuti a problemi di sicurezza informatica quali azioni sono previste dal tuo Comune?')
    options_4_4 = [
        'Gli incidenti vengono segnalati a un responsabile designato per la gestione (DPO, RTD, responsabile IT, amministratore di sistema)',
        'Viene attivato un team di risposta agli incidenti informatici (CSIRT) per risolvere il problema',
        'SI segue un protocollo specifico di gestione degli incidenti informatici',
        'Altro'
    ]
    selected_4_4 = multiple_choice_question('Seleziona una o più opzioni:', options_4_4, key='4_4')
    if 'Altro' in selected_4_4:
        st.text_input('Specificare:', key='4_4_other')
