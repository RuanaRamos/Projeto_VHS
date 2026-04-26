import streamlit as st
from VHAS import responder_pergunta  # Aqui conectamos os dois arquivos!

st.set_page_config(page_title="Projeto VHaS", page_icon="🤖")
st.title("🤖 Assistente VHaS (Versatile Handling Solution)")

# --- BARRA LATERAL PARA IDIOMA ---
with st.sidebar:
    st.title("Configurações")
    idioma = st.selectbox(
        "Choose your language:",
        ["Português", "English", "Español", "Deutsch", "Français"]
    )
    st.info(f"O assistente responderá em {idioma}")

st.title("🤖 Assistente VHS")

# Histórico de conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra as mensagens na tela
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if prompt := st.chat_input("Como posso ajudar?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Consultando manual..."):
            #O IDIOMA AQUI!
            resposta = responder_pergunta(prompt, idioma) 
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})