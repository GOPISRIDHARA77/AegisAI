from app.rag.embedding import create_embeddings 

def retrieve(query:str,chunks: list[str],vectore_store,top_k: int = 3,):
    query_embedding = create_embeddings([query])[0]
    distance,indices = vectore_store.search(query_embedding,top_k,)

    retrieved_chunks = []

    for index in indices[0]:
        if index != -1:
            retrieved_chunks.append(chunks[index])
    return retrieved_chunks
