from app.rag.pipeline import process_documents
from app.rag.retriever import retrieve
from app.rag.generator import generate_answer

documents=process_documents()
document = documents[0]
query = "How many paid leaves do employee get?"

retrieved_chunk = retrieve(query,document["chunks"],document["vector_store"],top_k=2,)

context = "\n\n".join(retrieved_chunk)
answer = generate_answer(query,context,)

print("\nUSER QUESTION:")
print(query)

print("\nRETRIEVED CONTEXT:")
print(context)

print("\nFINAL ANSWER:")
print(answer)