from app.rag.pipeline import process_documents 
from app.rag.retriever import retrieve 

def test_retrieve():
    documents = process_documents()

    document = documents[0]

    results = retrieve("How many paid leaves do employees get?",document["chunks"],document["vector_store"],top_k=2,)

    assert len(results)>0