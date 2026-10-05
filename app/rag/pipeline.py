from app.rag.document_loader import load_documents 
from app.rag.document_cleaner import clean_text 

def load_and_clean_documents():
    documents = load_documents()

    for document in documents:
        document["text"] = clean_text(document["text"])
    return documents