from app.rag.document_cleaner import clean_text


def test_clean_text():
    raw_text = "AegisAI   Company Policy\n\n\nWorking Hours:   9 AM to 6 PM"

    cleaned_text = clean_text(raw_text)

    assert "AegisAI Company Policy" in cleaned_text
    assert "\n\n\n" not in cleaned_text
    assert "Working Hours: 9 AM to 6 PM" in cleaned_text