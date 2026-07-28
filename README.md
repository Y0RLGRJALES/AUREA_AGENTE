# 💄 AUREA - Agente Inteligente para Consulta de Documentos

## Descripción

AUREA es un asistente virtual desarrollado mediante la arquitectura **Retrieval-Augmented Generation (RAG)**, diseñado para responder preguntas utilizando exclusivamente la información contenida en documentos PDF de una tienda de cosméticos.

El sistema recupera los fragmentos más relevantes mediante búsqueda semántica y genera respuestas utilizando el modelo **Llama 3.3 70B Versatile**, accedido a través de la API de **Groq**.

---

# Arquitectura del sistema

```
                Usuario
                    │
                    ▼
             Pregunta en Streamlit
                    │
                    ▼
          Recuperación de documentos
               (Retriever MMR)
                    │
                    ▼
        ChromaDB + Sentence Transformers
                    │
                    ▼
         Fragmentos más relevantes
                    │
                    ▼
        Modelo Llama 3.3 70B (Groq)
                    │
                    ▼
               Respuesta final
```

---

# Tecnologías utilizadas

- Python 3.11+
- Streamlit
- LangChain
- ChromaDB
- Sentence Transformers
- Groq API
- Llama 3.3 70B Versatile
- PyPDF

---

# Estructura del proyecto

```
AUREA_AGENTE/
│
├── app.py
├── rag.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── documentos/
│     ├── catalogo.pdf
│     └── promociones.pdf
└── AUREA_AGENT.ipynb
```

---

# Instalación

Clonar el repositorio

```bash
git clone https://github.com/Y0RLGRJALES/AUREA_AGENTE.git
```

Entrar al proyecto

```bash
cd AUREA_AGENTE
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación

```bash
streamlit run app.py
```

---

# Configuración

Antes de ejecutar la aplicación debes configurar la variable:

```
GROQ_API_KEY
```

En Streamlit Community Cloud se configura desde:

```
Settings
→ Secrets
```

Ejemplo:

```toml
GROQ_API_KEY="TU_API_KEY"
```

---

# Funcionamiento

El sistema realiza el siguiente flujo:

1. Carga todos los documentos PDF.
2. Divide los documentos en fragmentos (chunks).
3. Genera embeddings utilizando Sentence Transformers.
4. Construye una base vectorial con ChromaDB.
5. Recupera los fragmentos más relevantes mediante búsqueda MMR.
6. Envía únicamente esos fragmentos al modelo Llama 3.3.
7. Genera una respuesta basada exclusivamente en el contexto recuperado.

---

# Ejemplos de consultas

- ¿Tienen envío gratis?
- ¿Aceptan PSE?
- ¿Qué promociones tienen disponibles?
- ¿Cuáles son las políticas de devolución?
- ¿Qué productos manejan?

---

# Ejemplo de respuesta

**Pregunta**

```
¿Aceptan PSE?
```

**Respuesta**

```
Sí. Según la información encontrada en los documentos oficiales...
```

**Fuentes**

- catalogo.pdf

---

# Despliegue

La aplicación fue desplegada mediante **Streamlit Community Cloud**.

Enlace:

```
(Pegar aquí el enlace de Streamlit cuando realices el deploy)
```

---

# Capturas de pantalla

Agregar las siguientes imágenes:

- Aplicación ejecutándose localmente.
- Aplicación desplegada en Streamlit.
- Respuesta generada por el agente.

---

# Autor

**Yorlandi Grajales**

Proyecto académico sobre arquitecturas **Retrieval-Augmented Generation (RAG)** utilizando LangChain, ChromaDB y Groq.

---

