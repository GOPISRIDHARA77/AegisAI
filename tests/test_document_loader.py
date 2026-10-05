from app.rag.document_loader import load_documents

def test_load_documents():
    documents = load_documents()

    assert len(documents) == 1
    assert documents[0]["source"] == "company_policy.txt"
    assert "Working Hours" in documents[0]["text"]