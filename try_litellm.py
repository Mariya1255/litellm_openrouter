import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

def main():
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

    if not openrouter_api_key:
        print("Error: OPENROUTER_API_KEY not found!")
        return

    response = completion(
        model="mistralai/mistral-7b-instruct",
        api_key=openrouter_api_key,
        api_base="https://openrouter.ai/api/v1",
        messages=[
            {
                "role": "user",
                "content": "Hello! Please say hello back and tell me one interesting fact about AI.",
            }
        ],
        max_tokens=100,
        temperature=0.7,
    )

    print("LiteLLM Response:")
    print("=" * 40)
    print(response.choices[0].message.content)
    print("=" * 40)
    print(f"Model used: {response.model}")
    if hasattr(response, "usage") and response.usage:
        print(f"Tokens used: {response.usage.total_tokens}")

if __name__ == "__main__":
    main()
