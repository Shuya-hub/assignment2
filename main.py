import os
from dotenv import load_dotenv
from groq import Groq

def main():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ GROQ_API_KEY not found.")
        return

    client = Groq(api_key=api_key)
    print("🌐 Chat interface to Groq. Type 'quit' to exit.")
    history = []

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("👋 Goodbye!")
            break
        history.append({"role": "user", "content": user_input})
        try:
            completion = client.chat.completions.create(
                messages=history,
                model="openai/gpt-oss-20b",
            )
            assistant_text = completion.choices[0].message.content
            print(f"AI: {assistant_text}")
            history.append({"role": "assistant", "content": assistant_text})
        except Exception as e:
            print("❌ API call failed:", e)

if __name__ == "__main__":
    main()
