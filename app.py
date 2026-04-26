import streamlit as st
from VHAS import responder_pergunta  # Hier verbinden wir die beiden Dateien!

st.set_page_config(page_title="Projekt VHaS", page_icon="🤖")
st.title("🤖 VHaS Assistent (Versatile Handling Solution)")

# --- SEITENLEISTE FÜR SPRACHE ---
with st.sidebar:
    st.title("Einstellungen")
    idioma = st.selectbox(
        "Wählen Sie Ihre Sprache:",
        ["Deutsch", "English", "Español", "Português", "Français"]
    )
    st.info(f"Der Assistent wird auf {idioma} antworten")

st.title("🤖 VHS Assistent")

# Verlauf der Konversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Nachrichten auf dem Bildschirm anzeigen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Benutzereingabe
if prompt := st.chat_input("Wie kann ich helfen?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Handbuch wird konsultiert..."):
            # DIE SPRACHE HIER!
            resposta = responder_pergunta(prompt, idioma) 
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})
