from app.rag.embedding import create_embeddings 

def test_create_embeddings ():
    chunks = [
        "Employees receive 18 paid leaves per year.",
        "Emplyees work from 9 AM to 6 PM.",
    ]

    embeddings = create_embeddings(chunks)

    assert len(embeddings) == 2

    