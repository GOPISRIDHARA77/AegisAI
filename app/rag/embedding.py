from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-l6-v2") # loads a pretrained embedding model locally

def create_embeddings(chunks: list[str]):
    embeddings = model.encode(chunks)

    return embeddings