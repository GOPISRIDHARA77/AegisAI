import faiss
import numpy as np 

class VectorStore:
    def __init__(self,dimension: int):
        self.index = faiss.IndexFlatL2(dimension) # creates a faiss vector index

    def add_embeddings(self,embeddings):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)

    def search(self,query_embeddings,top_k: int = 3):
        query_vector = np.array([query_embeddings]).astype("float")

        distances,indices = self.index.search(query_vector,top_k,)

        return distances,indices
    