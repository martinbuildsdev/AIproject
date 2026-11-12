
import os
import argparse
import json
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_functions import available_functions, call_function

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
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

for _ in range(20):
# Send a message to AI
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )
    if response.usage is None:
        raise RuntimeError("Failed API reguest")


# Print AI response
    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")


    message = response.choices[0].message
    messages.append(message)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, args.verbose)
            messages.append(result_message)
            if not result_message["content"]:
                raise Exception("Function call returned empty content")
            print(f"-> {result_message['content']}")
            
    else:
        print(message.content)
        break
else:
    print("Agent reached the maximum number of iterations without a final response.")
