import streamlit as st

# Function to create multiple-choice questions
def multiple_choice_question(question, options):
    return st.multiselect(question, options)

# Function to create radio button questions
def radio_button_question(question, options):
    return st.radio(question, options)

# Function to create text input questions
def text_input_question(question):
    return st.text_input(question)

# Function to create number input questions
def number_input_question(question):
    return st.number_input(question, min_value=0, step=1)

# Function to create conditional text input
def conditional_text_input(question, condition):
    if condition:
        return st.text_input(question)

# Function to create Likert scale questions
def likert_scale_question(question, options):
    return st.radio(question, options)

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
selected_2_1 = multiple_choice_question('Seleziona una o più opzioni:', options_2_1)
conditional_text_input('Specificare:', 'Altro' in selected_2_1)

# Question 2.2
st.subheader('2.2 Il tuo Comune è socio di una società pubblica che si occupa di fornire servizi ICT?')
options_2_2 = [
    'SI, il mio Comune possiede una quota societaria di una società di servizi con competenze ICT',
    'SI, il mio Comune è socio unico di una società di servizi con competenze ICT',
    'NO, il mio Comune non gestisce una propria società di servizi con competenze ICT'
]
selected_2_2 = radio_button_question('Seleziona un\'opzione:', options_2_2)

# Question 2.3
st.subheader('2.3 Il tuo Comune come gestisce i servizi ICT?')
options_2_3 = [
    'Il Comune gestisce autonomamente in tutto o in parte i sistemi ICT',
    'Il Comune si avvale di uno o più fornitori esterni per i servizi ICT',
    'Il Comune ha una propria società in-house che gestisce i servizi ICT',
    'Non sono disponibili informazioni sul modello di gestione ICT del Comune',
    'Il Comune partecipa a una gestione ICT associata con altri enti pubblici'
]
selected_2_3 = multiple_choice_question('Seleziona una o più opzioni:', options_2_3)

# Question 2.4
st.subheader('2.4 In merito alla gestione dei servizi ICT indica il numero di risorse IT che sono previste in pianta organica nel tuo Comune.')
num_resources_planned = number_input_question('Numero di risorse IT previste:')

# Conditional Questions 2.4.1 to 2.4.3 based on previous answers
if num_resources_planned > 0:
    num_resources_operational = number_input_question('Numero di risorse IT effettivamente operativo:')
    if num_resources_planned != num_resources_operational:
        reasons_for_difference = multiple_choice_question(
            'Quali sono le ragioni principali che causano una differenza tra il personale IT previsto e quello realmente disponibile?',
            ['Mancanza di fondi', 'Difficoltà nel reperimento di personale qualificato', 'Vincoli normativi', 'Altri motivi']
        )
        conditional_text_input('Specificare:', 'Altri motivi' in reasons_for_difference)

    resource_types = multiple_choice_question(
        'In merito al personale IT indica la tipologia delle risorse selezionando una o più opzioni.',
        ['Interno all’ente', 'Condiviso con altri Enti', 'Esterno']
    )

# Question 2.5 to 2.14
# You can similarly add other questions following the same pattern

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
selected_3_1 = radio_button_question('Seleziona un\'opzione:', options_3_1)

# Continue with other questions similarly...

# Section 4: Sicurezza
st.header('4. Sicurezza')

# Example Question in Section 4
st.subheader('4.1 Come è gestito il backup dei dati e dei sistemi nel tuo Comune?')
options_4_1 = ['Tramite backup locale', 'Tramite backup in cloud', 'Utilizzando entrambe le modalità: locale e in cloud']
selected_4_1 = radio_button_question('Seleziona un\'opzione:', options_4_1)

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

if __name__ == '__main__':
    st.run()
