import streamlit as st
from rag import AureaRAG

# ---------------------------------------------------
# Configuración de la página
# ---------------------------------------------------

st.set_page_config(
    page_title="AUREA",
    page_icon="💄",
    layout="wide"
)

# ---------------------------------------------------
# Título
# ---------------------------------------------------

st.title("💄 AUREA")
st.subheader("Asistente Inteligente para Cosméticos")

st.markdown("""
Realiza preguntas sobre los documentos cargados.

El asistente responderá únicamente con la información encontrada en los PDF.
""")

# ---------------------------------------------------
# Verificar API KEY
# ---------------------------------------------------

if "GROQ_API_KEY" not in st.secrets:
    st.error("No se encontró la variable GROQ_API_KEY en los Secrets de Streamlit.")
    st.info("Agrega tu API Key antes de ejecutar la aplicación.")
    st.stop()

# ---------------------------------------------------
# Cargar el agente solo una vez
# ---------------------------------------------------

@st.cache_resource
def cargar_agente():
    return AureaRAG(
        groq_api_key=st.secrets["GROQ_API_KEY"]
    )

try:
    agente = cargar_agente()
except Exception as e:
    st.error(f"Error al cargar el agente:\n\n{e}")
    st.stop()

# ---------------------------------------------------
# Entrada de la pregunta
# ---------------------------------------------------

pregunta = st.text_input(
    "Escribe tu pregunta:",
    placeholder="Ejemplo: ¿Tienen envío gratis?"
)

# ---------------------------------------------------
# Botón consultar
# ---------------------------------------------------

if st.button("Consultar"):

    if pregunta.strip() == "":
        st.warning("Por favor escribe una pregunta.")
        st.stop()

    with st.spinner("Buscando información..."):

        resultado = agente.preguntar(pregunta)

    st.success("Respuesta")

    st.write(resultado["respuesta"])

    if resultado["fuentes"]:

        st.divider()

        st.subheader("📄 Fuentes consultadas")

        for fuente in resultado["fuentes"]:
            st.write(f"• {fuente}")

# ---------------------------------------------------
# Barra lateral
# ---------------------------------------------------

with st.sidebar:

    st.title("💄 AUREA")

    st.markdown("""
### Asistente Inteligente

Este proyecto implementa un agente basado en **Retrieval-Augmented Generation (RAG)**.

### Tecnologías

- Python
- Streamlit
- LangChain
- ChromaDB
- Sentence Transformers
- Groq
- Llama 3.3 70B

### Flujo

PDFs → Chunks → Embeddings → ChromaDB → Retriever → LLM → Respuesta

---

**Autor:** Yorlandi Grajales
""")
