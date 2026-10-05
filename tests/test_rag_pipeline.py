from app.rag.pipeline import load_and_clean_documents


def test_load_and_clean_documents():
    documents = load_and_clean_documents()

    assert len(documents) == 1
    assert documents[0]["source"] == "company_policy.txt"
    assert "\n\n\n" not in documents[0]["text"]
    assert "Working Hours" in documents[0]["text"]