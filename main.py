
import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.environ.get("OPENROUTER_API_KEY")

# Check if API key exists
if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY not found. Please add it to your .env file.")

# Create OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`
messages = [
    {"role": "user", "content": args.user_prompt},
]

# Send a message to AI
response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)
if response.usage is None:
    raise RuntimeError("Failed API reguest")


# Print AI response
if args.verbose == True:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")


print(response.choices[0].message.content)

