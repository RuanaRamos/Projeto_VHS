import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


# --- 1. CARREGAR SEGREDOS ---
load_dotenv()
chave_api = os.getenv("GROQ_API_KEY")

# --- 2. CONFIGURAÇÃO DO MODELO (GROQ) ---
llm = ChatGroq(
    api_key=chave_api,
    model_name="llama-3.3-70b-versatile",
    temperature=0.4
)

# --- 3. CARREGAR O PDF ---
caminho_pdf = "Manual_Tecnico_VHaS_.pdf"
loader = PyPDFLoader(caminho_pdf)
documentos = loader.load()

# --- 4. PREPARAR O BANCO DE DADOS (RAG) ---
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
chunks = text_splitter.split_documents(documentos)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever()

# --- 5. PROMPT TEMPLATE (Sua personalização) ---
template = """
Você é o assistente técnico do Projeto VHS (Versatile Handling Solution).
Sua missão é ajudar trabalhadores de armazém que estão com medo de errar ou digitar algo errado.
Use os pedaços de contexto do manual abaixo para responder à pergunta de forma simples.

REGRAS:
1. Explique como se estivesse falando com uma criança de 10 anos sem termos tecnicos dificeis.
2. Se houver um termo técnico, coloque a função/tradução ao lado.
3. Se não souber a resposta baseada no manual, peça para chamar o supervisor.
4. Seja direto nas respostas. nao coloque muitas informacoes, no maximo 4 linhas.

CONTEXTO:
{context}

PERGUNTA DO TRABALHADOR:
{question}

RESPOSTA DIDÁTICA:
"""

prompt = PromptTemplate.from_template(template)

# --- 6. CHAIN (O Fluxo de Trabalho) ---
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# --- 7. EXECUÇÃO NO TERMINAL ---
def responder_pergunta(pergunta_usuario, idioma_escolhido):
    try:
        instrucao_idioma = f"\n\nIMPORTANTE: Responda obrigatoriamente no idioma: {idioma_escolhido}."
        
        # O rag_chain processa a pergunta com a instrução de língua
        resposta = rag_chain.invoke(pergunta_usuario + instrucao_idioma)
        return resposta
    except Exception as e:
        return f"Erro ao processar: {e}"