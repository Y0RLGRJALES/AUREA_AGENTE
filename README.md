# AUREA - Agente Inteligente para Consulta de Documentos

## Descripción

AUREA es un asistente virtual basado en la arquitectura Retrieval-Augmented Generation (RAG), diseñado para responder preguntas utilizando exclusivamente la información contenida en documentos PDF de una tienda de cosméticos.

El sistema recupera los fragmentos más relevantes mediante búsqueda semántica y genera respuestas utilizando el modelo Llama 3.3 70B Versatile a través de la API de Groq.

---

# Arquitectura

Usuario

↓

Pregunta

↓

Retriever (ChromaDB)

↓

Embeddings (Sentence Transformers)

↓

Fragmentos relevantes

↓

LLM (Llama 3.3 70B - Groq)

↓

Respuesta

---

# Tecnologías

- Python
- Google Colab
- LangChain
- ChromaDB
- Sentence Transformers
- Groq API
- Llama 3.3 70B
- PyPDF

---

# Flujo del proyecto

1. Cargar documentos PDF.
2. Dividir el contenido en fragmentos.
3. Generar embeddings.
4. Crear la base vectorial con ChromaDB.
5. Recuperar los fragmentos más relevantes.
6. Construir el contexto.
7. Enviar el contexto al modelo LLM.
8. Generar una respuesta basada únicamente en la información recuperada.

---

# Instalación

```bash
git clone https://github.com/Y0RLGRJALES/AUREA_AGENTE.git

cd AUREA_AGENTE
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Configuración

Crear una API Key en Groq.

Guardar la variable:

```
GROQ_API_KEY
```

En Google Colab puede almacenarse utilizando Secrets.

---

# Ejemplo de uso

```python
preguntar_aurea("¿Tienen envío gratis?")
```

Respuesta esperada

```
Sí. La tienda ofrece envío gratuito para compras superiores al valor indicado en el documento oficial.
```

Otro ejemplo

```python
preguntar_aurea("¿Aceptan PSE?")
```

---

# Arquitectura RAG

```
PDFs
      │
      ▼
Carga de documentos
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
ChromaDB
      │
      ▼
Retriever
      │
      ▼
Contexto
      │
      ▼
Groq
      │
      ▼
Respuesta
```

---

# Ejemplos de preguntas

- ¿Aceptan PSE?
- ¿Hay envío gratis?
- ¿Cuánto tarda el despacho?
- ¿Qué productos están disponibles?
- ¿Cuáles son las políticas de devolución?

---

# Resultados

El agente responde únicamente utilizando la información contenida en los documentos cargados, evitando generar respuestas inventadas (hallucinations).

---

# Capturas

Agregar aquí una captura del notebook funcionando.

Agregar aquí una captura del despliegue en OCI.

---

# Autor

Yorlandi Grajales

Proyecto académico - Arquitectura RAG con LangChain, ChromaDB y Groq.
