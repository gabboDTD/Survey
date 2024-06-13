import streamlit as st

# Function to create multiple-choice questions
def multiple_choice_question(question, options, key):
    return st.multiselect(question, options, key=key)

# Function to create radio button questions
def radio_button_question(question, options, key):
    return st.radio(question, options, key=key)

# Function to create text input questions
def text_input_question(question, key):
    return st.text_input(question, key=key)

# Function to create number input questions
def number_input_question(question, key):
    return st.number_input(question, min_value=0, step=1, key=key)

# Function to create conditional text input
def conditional_text_input(question, condition, key):
    if condition:
        return st.text_input(question, key=key)

# Function to create Likert scale questions
def likert_scale_question(question, options, key):
    return st.radio(question, options, key=key)

# Survey Title and Introduction
st.title('Survey 2024 - Mappa dei Comuni Digitali')
st.write("""
La survey 2024 mira ad indagare specifici aspetti dell’informatizzazione e della digitalizzazione dei Comuni.
Le domande sono strutturate in modo da ridurre al minimo la richiesta di informazioni già potenzialmente disponibili,
cercando di rilevare quegli elementi utili per l’integrazione e la qualificazione delle informazioni già in possesso del DTD e di ANCI.
""")

# Section 1: Anagrafica (TBD)
st.header('1. Anagrafica')

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

# Question 2.13
st.subheader('2.13 In merito alla formazione sulle competenze digitali del personale del tuo Comune indica il livello di supporto necessario per ciascuna delle voci seguenti.')

competencies = ['Utilizzo di software specifici', 'Gestione dei dati digitali', 'Comunicazione su canali digitale', 'Sicurezza informatica', 'Programmazione', 'Utilizzo di piattaforme collaborative', 'Analisi dei dati']
support_levels = ['Nessun supporto necessario', 'Supporto minimo', 'Supporto moderato', 'Supporto significativo']

for i, competency in enumerate(competencies):
    st.write(competency)
    likert_scale_question('', support_levels, key=f'2_13_{i}')

# Question 2.14
st.subheader('2.14 Nell’ambito della formazione ICT che il tuo Comune offre ai dipendenti indica per ciascuna delle voci seguenti se il corso è obbligatorio, opzionale, o non previsto.')

training_topics = ['Corso base (ad esempio strumenti MSFT Office, fogli di calcolo, accesso al cloud ecc.)', 'Corsi gestione dei dati (es. dati aperti)', 'Corsi di gestione di infrastrutture complesse di servizi digitali', 'Corsi su piattaforme specializzate (ad esempio GIS, e-procurement ecc.)', 'Altro (specificare)']
training_options = ['Obbligatorio', 'Opzionale', 'Non previsto']

for i, topic in enumerate(training_topics):
    st.write(topic)
    likert_scale_question('', training_options, key=f'2_14_{i}')

# Section 3: Infrastruttura ICT
st.header('3. Infrastruttura ICT')

# Example Question in Section 3
st.subheader('3.1 Allo stato attuale nel tuo Comune sono operativi server fisici per la gestione e l’utilizzo di applicazioni e dati?')
options_3_1 = [
    'SI esistono server attivi all’interno del Comune per la gestione di applicazioni e dati',
    'NO non sono più previsti server installati presso il Comune poiché è stata completata la migrazione al cloud',
    'NO non è più attivo un server per la gestione di applicazioni e dati ma sono attivi alcuni sistemi per la gestione e la protezione della rete e degli accessi',
    'NO le applicazioni sono state già migrate sul cloud ma il file server con documenti dati immagini ecc. sono archiviati in locale in cartelle condivise.'
]
selected_3_1 = radio_button_question('Seleziona un\'opzione:', options_3_1, key='3_1')

# Continue with other questions similarly...

# Section 4: Sicurezza
st.header('4. Sicurezza')

# Example Question in Section 4
st.subheader('4.1 Come è gestito il backup dei dati e dei sistemi nel tuo Comune?')
options_4_1 = ['Tramite backup locale', 'Tramite backup in cloud', 'Utilizzando entrambe le modalità: locale e in cloud']
selected_4_1 = radio_button_question('Seleziona un\'opzione:', options_4_1, key='4_1')

# Continue with other questions similarly...

# Add sections for other parts of the survey as needed...

# Section 5: Servizi I (Protocollo Atti Segreteria generale URP)
# Section 6: Servizi II (Ragioneria Tributi Patrimonio)
# Section 7: Servizi III (Servizi sociali Servizi scolastici)
# Section 8: Servizi IV (Sportelli Unici SUAP SUE)
# Section 9: Servizi V (Territorio Ambiente lavoro)
# Section 10: Servizi VI (Demografici Personale Servizi cimiteriali)
# Section 11: Servizi VII (Polizia locale)
# Section 12: Applicazioni & Dati
# Section 13: Servizi Digitali
# Section 14: Atti & Procedimenti Amministrativi
# Section 15: Governance
# Section 16: Innovazione

# Submit button
if st.button('Submit'):
    st.write('Thank you for completing the survey!')
