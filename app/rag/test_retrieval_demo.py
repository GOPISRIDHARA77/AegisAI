from app.rag.pipeline import process_documents 
from app.rag.retriever import retrieve 

documents = process_documents()

document = documents[0]
query = "How many paid leaves do employee get?"

results = retrieve(query,document["chunks"],document["vector_store"],top_k=2,)

print("\n USER QUESTION:")
print(query)

for chunk in results:
    print("\n----")
    print(chunk)