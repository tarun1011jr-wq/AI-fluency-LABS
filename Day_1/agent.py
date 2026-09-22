import json

from config import client, MODEL
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a college assistant.

Important rules:
1. Never guess course fees.
2. Always use get_course_fee when a course fee is needed.
3. Use calculator for arithmetic.
4. Available course codes are CS101, AI202, and DS303.
5. If no tool is needed, answer directly.
"""


def agent(question, max_steps=6):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(max_steps):

        print(f"\n--- Agent Step {step + 1} ---")

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )

        message = response.choices[0].message

        # No tool needed → final answer
        if not message.tool_calls:

            print("No tool call needed.")

            return message.content

        # Add the assistant's tool request to conversation
        messages.append(message)

        # Execute every requested tool
        for tool_call in message.tool_calls:

            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(f"Tool requested: {function_name}")
            print(f"Arguments: {arguments}")

            if function_name not in TOOL_FUNCTIONS:
                result = f"Unknown tool: {function_name}"

            else:
                function = TOOL_FUNCTIONS[function_name]
                result = function(**arguments)

            print(f"Tool result: {result}")

            # Give tool result back to the LLM
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )

    return "Agent stopped: maximum steps reached."


if __name__ == "__main__":

    questions = [
        "What is the fee for AI202?",
        "What is the total fee for CS101 and AI202 after a 10% scholarship?",
        "Is DS303 more expensive than CS101, and by how much?",
        "Write a two-line welcome message for new AI students."
    ]

    print("=" * 60)
    print("SYSTEM 3 - AI AGENT")
    print("=" * 60)

    for i, question in enumerate(questions, start=1):

        print(f"\nQ{i}: {question}")
        print("-" * 60)

        answer = agent(question)

        print("\nFinal Answer:")
        print(answer)