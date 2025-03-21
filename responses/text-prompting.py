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


# --------------------------------------------------------------
# Introducing instructions
# --------------------------------------------------------------

"""
Inputs can now be a single string or a list of messages.

The list of roles can now be:
- system
- developer
- user
- assistant
"""

response = client.responses.create(
    model="gpt-4o",
    instructions="Talk like a pirate.",
    input="Are semicolons optional in JavaScript?",
)

print(response.output_text)


# Which would be similar to:


response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "developer", "content": "Talk like a pirate."},
        {"role": "user", "content": "Are semicolons optional in JavaScript?"},
    ],
)

print(response.output_text)


# The chain of command (hierarchical instructions)
# In this example, the developer is telling the system to talk like a pirate, and the system is telling the developer to not talk like a pirate.
# system will overide the developer prompt
response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "system", "content": "Talk like a pirate."},
        {"role": "developer", "content": "don't talk like a pirate."},
        {"role": "user", "content": "Are semicolons optional in JavaScript?"},
    ],
)

print(response.output_text)  # talks like a pirate

response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "system", "content": "Don't talk like a pirate."},
        {"role": "developer", "content": "Talk like a pirate."},
        {"role": "user", "content": "Are semicolons optional in JavaScript?"},
    ],
)

print(response.output_text)  # doesn't talk like a pirate


# --------------------------------------------------------------
# so Hierarchical instructions will be system > developer > user> assistant
