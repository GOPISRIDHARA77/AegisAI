from transformers import AutoTokenizer,AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def generate_answer(query:str,context:str):
    prompt = f""""
    Answer the question using only the provided context.
    context:
    {context}

    Question:
    {query}

    Answer:
    """

    inputs = tokenizer(prompt,return_tensors="pt")
    outputs = model.generate(**inputs,max_new_tokens=50,)
    answer = tokenizer.decode(outputs[0],skip_special_tokens=True,)

    return answer

 
