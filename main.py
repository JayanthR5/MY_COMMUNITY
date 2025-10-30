from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about sustainability, recycling, and proper waste disposal.

Here are some relevant sustainability facts from your knowledge base: 
{context}

Here is the question to answer: {question}

Please provide a clear, concise, and environmentally responsible answer.
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Ask your sustainability question (q to quit): ")
    print("\n\n")
    if question.lower() == "q":
        break

    context = retriever.invoke(question)
    result = chain.invoke({"context": context, "question": question})
    print(result)