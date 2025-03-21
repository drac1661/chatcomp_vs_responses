from openai import OpenAI
import openai
import os
from dotenv import load_dotenv

openai.api_base = os.getenv("base_url")
openai.api_key = os.getenv("OPENAI_API_KEY")

load_dotenv()


client = OpenAI(
    base_url=os.getenv("base_url"),
    api_key=os.getenv("OPENAI_API_KEY"),
)


response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a fairytales.",
        }
    ],
)

print(response.choices[0].message.content)


# --------------------------------------------------------------
# Basic text example with the Responses API
# --------------------------------------------------------------

response = client.responses.create(
    model="gpt-4o", input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)

# responses api will also work in old fashion of defining role in dictionary format
response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "user", "content": "what teams are playing in this image?"},
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg",
                }
            ],
        },
    ],
)

print(response.output_text)


stream = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn.",
    stream=True,
)

# Store chunks in a list
text_chunks = []

for event in stream:
    if hasattr(event, "type") and "text.delta" in event.type:
        text_chunks.append(event.delta)
        print(event.delta, end="", flush=True)
