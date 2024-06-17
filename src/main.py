import streamlit as st
from section_1 import display_section_1
from section_2 import display_section_2
from section_3 import display_section_3
from section_4 import display_section_4
from section_5 import display_section_5
from section_6 import display_section_6
from section_7 import display_section_7

from section_10 import display_section_10
from section_11 import display_section_11

# Survey Title and Introduction
st.title('Survey 2024 - Mappa dei Comuni Digitali')

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["INTRODUZIONE",
                                     "ANAGRAFICA",
                                     "ORGANIZZAZIONE DELL'ENTE E DEI SERVIZI", 
                                     "INFRASTRUTTURA ICT",
                                     "SICUREZZA",
                                     "SERVIZI I (Protocollo, Atti, Segreteria generale, URP)",
                                     "SERVIZI II (Ragioneria, Tributi, Patrimonio)",
                                     "SERVIZI III (Servizi sociali Servizi scolastici)",
                                     "SERVIZI VI (Demografici, Personale, Servizi cimiteriali)",
                                     "SERVIZI VII (Polizia locale)"
                                     ])

# Display the selected section
if section == "INTRODUZIONE":
    st.write("""
    La survey 2024 mira ad indagare specifici aspetti dell’informatizzazione e della digitalizzazione dei Comuni.
    Le domande sono strutturate in modo da ridurre al minimo la richiesta di informazioni già potenzialmente disponibili,
    cercando di rilevare quegli elementi utili per l’integrazione e la qualificazione delle informazioni già in possesso del DTD e di ANCI.
    """)
elif section == "ANAGRAFICA":
    display_section_1()
elif section == "ORGANIZZAZIONE DELL'ENTE E DEI SERVIZI":
    display_section_2()
elif section == "INFRASTRUTTURA ICT":
    display_section_3()
elif section == "SICUREZZA":
    display_section_4()
elif section == "SERVIZI I (Protocollo, Atti, Segreteria generale, URP)":
    display_section_5()
elif section == "SERVIZI II (Ragioneria, Tributi, Patrimonio)":
    display_section_6()
elif section == "SERVIZI III (Servizi sociali Servizi scolastici)":
    display_section_7()
elif section == "SERVIZI VI (Demografici, Personale, Servizi cimiteriali)":
    display_section_10()
elif section == "SERVIZI VII (Polizia locale)":
    display_section_11()

# Section 1: Anagrafica (TBD)
# st.header('1. Anagrafica')

# # Display Section 2: Organizzazione
# display_section_2()

# # Display Section 3: Infrastruttura ICT
# display_section_3()

# # Display Section 4: Sicurezza
# display_section_4()

# # Display Section 5: Servizi I (Protocollo, Atti, Segreteria, URP)
# display_section_5()

# Display Section 6: Servizi II (Ragioneria, Tributi, Patrimonio)
# display_section_6()

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