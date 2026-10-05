from app.rag.chunker import chunk_text

def test_chunk_text():
    text="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chunks = chunk_text(
        text,
        chunk_size=10,
        overlap = 2
    )

    assert len(chunks)>1
    assert chunks[0] == "ABCDEFGHIJ"
    assert chunks[1][:2] == "IJ"