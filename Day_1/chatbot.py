from config import client, MODEL, QUESTIONS


def ask_llm(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful college assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content


print("=" * 60)
print("SYSTEM 1 - PLAIN LLM CHATBOT")
print("=" * 60)

for i, question in enumerate(QUESTIONS, start=1):
    print(f"\nQ{i}: {question}")
    print("-" * 60)

    answer = ask_llm(question)

    print("Answer:")
    print(answer)