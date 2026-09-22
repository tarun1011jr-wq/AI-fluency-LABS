from agent import agent

question = "I can pay Rs. 30,000. Which two courses can I take together within this budget?"

print("=" * 60)
print("CHALLENGE")
print("=" * 60)

print("\nQuestion:")
print(question)

print("\nAgent Processing:")
answer = agent(question)

print("\nFinal Answer:")
print(answer)