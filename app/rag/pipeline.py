from app.rag.document_loader import load_documents 
from app.rag.document_cleaner import clean_text 
from app.rag.chunker import chunk_text
from app.rag.embedding import create_embeddings 
from app.rag.vector_store import VectorStore

def process_documents():
    documents = load_documents()

    for document in documents:
        document["text"] = clean_text(document["text"])
        document["chunks"] = chunk_text(document["text"])
        document["embeddings"] = create_embeddings(document["chunks"])

        dimensions = len(document["embeddings"][0])
        vector_store = VectorStore(dimensions)
        vector_store.add_embeddings(document["embeddings"])
        document["vector_store"] = vector_store

    return documents