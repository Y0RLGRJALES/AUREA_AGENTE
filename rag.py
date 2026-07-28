import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from groq import Groq


class AureaRAG:

    def __init__(self, groq_api_key):

        self.client = Groq(api_key=groq_api_key)

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

        self.retriever = self._crear_retriever()

    def _crear_retriever(self):

        documentos = []

        carpeta = "documentos"

        if not os.path.exists(carpeta):
            raise Exception(
                "No existe la carpeta 'documentos'."
            )

        archivos = [
            archivo
            for archivo in os.listdir(carpeta)
            if archivo.lower().endswith(".pdf")
        ]

        if len(archivos) == 0:
            raise Exception(
                "No se encontraron archivos PDF dentro de la carpeta documentos."
            )

        for archivo in archivos:

            ruta = os.path.join(carpeta, archivo)

            loader = PyPDFLoader(ruta)

            docs = loader.load()

            for doc in docs:
                doc.metadata["source"] = archivo

            documentos.extend(docs)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(documentos)

        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )

        return vectordb.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 8,
                "fetch_k": 30,
                "lambda_mult": 0.3
            }
        )

    def generar(self, prompt):

        respuesta = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0,
            max_tokens=250,
            messages=[
                {
                    "role": "system",
                    "content": """
Eres AUREA.

Eres el asistente virtual oficial de una tienda online de cosméticos.

Tu única fuente de información es el contexto recibido.

Nunca inventes información.

Nunca utilices conocimientos externos.

Nunca deduzcas información.

Si la respuesta no aparece claramente en el contexto responde exactamente:

No encontré información oficial sobre esa consulta.
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return respuesta.choices[0].message.content.strip()

    def preguntar(self, pregunta):

        docs = self.retriever.invoke(pregunta)

        if not docs:
            return {
                "respuesta": "No encontré información oficial sobre esa consulta.",
                "fuentes": []
            }

        vistos = set()
        documentos = []

        for doc in docs:

            texto = doc.page_content.strip()

            if texto not in vistos:
                vistos.add(texto)
                documentos.append(doc)

        contexto = "\n\n".join(
            [
                f"DOCUMENTO {i+1}\n{doc.page_content}"
                for i, doc in enumerate(documentos)
            ]
        )

        prompt = f"""
CONTEXTO

{contexto}

PREGUNTA

{pregunta}

RESPUESTA
"""

        respuesta = self.generar(prompt)

        fuentes = list(
            dict.fromkeys(
                [
                    doc.metadata.get("source", "Desconocido")
                    for doc in documentos
                ]
            )
        )

        return {
            "respuesta": respuesta,
            "fuentes": fuentes
        }
