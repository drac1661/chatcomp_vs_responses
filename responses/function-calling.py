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




tools = [
    {
        "type": "function",
        "name": "send_email",
        "description": "Send an email to a given recipient with a subject and message.",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "The recipient email address."},
                "subject": {"type": "string", "description": "Email subject line."},
                "body": {"type": "string", "description": "Body of the email message."},
            },
            "required": ["to", "subject", "body"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gpt-4o",
    input="Can you send an email to drac@example.com  saying hi?",
    tools=tools,
)

print(response.output)
print(response.output[0].model_dump_json(indent=2))
print(response.output[1].model_dump_json(indent=2))
