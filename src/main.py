import streamlit as st
from section_2 import display_section_2
from section_3 import display_section_3
from section_4 import display_section_4

from utils import multiple_choice_question, radio_button_question, number_input_question, conditional_text_input

# Survey Title and Introduction
st.title('Survey 2024 - Mappa dei Comuni Digitali')
st.write("""
La survey 2024 mira ad indagare specifici aspetti dell’informatizzazione e della digitalizzazione dei Comuni.
Le domande sono strutturate in modo da ridurre al minimo la richiesta di informazioni già potenzialmente disponibili,
cercando di rilevare quegli elementi utili per l’integrazione e la qualificazione delle informazioni già in possesso del DTD e di ANCI.
""")

# Section 1: Anagrafica (TBD)
# st.header('1. Anagrafica')

# # Display Section 2
# display_section_2()

# # Display Section 3
# display_section_3()

# Display Section 3
display_section_4()

# # Section 3: Infrastruttura ICT
# st.header('3. Infrastruttura ICT')

# # Example Question in Section 3
# st.subheader('3.1 Allo stato attuale nel tuo Comune sono operativi server fisici per la gestione e l’utilizzo di applicazioni e dati?')
# options_3_1 = [
#     'SI esistono server attivi all’interno del Comune per la gestione di applicazioni e dati',
#     'NO non sono più previsti server installati presso il Comune poiché è stata completata la migrazione al cloud',
#     'NO non è più attivo un server per la gestione di applicazioni e dati ma sono attivi alcuni sistemi per la gestione e la protezione della rete e degli accessi',
#     'NO le applicazioni sono state già migrate sul cloud ma il file server con documenti dati immagini ecc. sono archiviati in locale in cartelle condivise.'
# ]
# selected_3_1 = radio_button_question('Seleziona un\'opzione:', options_3_1, key='3_1')

# # Continue with other questions similarly...

# # Section 4: Sicurezza
# st.header('4. Sicurezza')

# # Example Question in Section 4
# st.subheader('4.1 Come è gestito il backup dei dati e dei sistemi nel tuo Comune?')
# options_4_1 = ['Tramite backup locale', 'Tramite backup in cloud', 'Utilizzando entrambe le modalità: locale e in cloud']
# selected_4_1 = radio_button_question('Seleziona un\'opzione:', options_4_1, key='4_1')

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
    st.write('Grazie per aver completato la survey!')