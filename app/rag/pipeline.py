from app.rag.document_loader import load_documents 
from app.rag.document_cleaner import clean_text 
from app.rag.chunker import chunk_text
from app.rag.embedding import create_embeddings 

def process_documents():
    documents = load_documents()

    for document in documents:
        document["text"] = clean_text(document["text"])
        document["chunks"] = chunk_text(document["text"])
        document["embeddings"] = create_embeddings(document["chunks"])

    return documents