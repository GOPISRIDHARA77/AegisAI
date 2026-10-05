from app.rag.pipeline import process_documents


def test_process_documents():
    documents = process_documents()

    assert len(documents) == 1
    assert documents[0]["source"] == "company_policy.txt"
    assert len(documents[0]["chunks"]) > 1 
    assert "Working Hours" in documents[0]["chunks"][0]