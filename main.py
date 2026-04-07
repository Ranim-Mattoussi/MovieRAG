from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template ="""
You are an expert in answering questions about movies from the IMDB Top 1000 list.

Here are some movie descriptions : {reviews}

here is the question to answer : {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model



while True:
    print("\n" + "-" * 50)
    
    question = input("Ask your question (type 'q' to quit): ").strip()

    if question.lower() in ['q', 'quit', 'exit']:
        print("👋 Exiting... Goodbye!")
        break

    if not question:
        print("⚠️ Please enter a valid question.")
        continue

    print("\n🔎 Searching relevant reviews...")

    try:
        reviews = retriever.invoke(question)

        result = chain.invoke({
            "reviews": reviews,
            "question": question
        })

        print("\n🧠 Answer:")
        print(result)

    except Exception as e:
        print(f"❌ Error: {e}")