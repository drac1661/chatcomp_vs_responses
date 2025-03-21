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

"""
https://platform.openai.com/docs/guides/conversation-state?api-mode=responses
"""



response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "user", "content": "knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Divyansha"},
    ],
)

print(response.output_text)

#
# Dynamic conversation state



history = [{"role": "user", "content": "tell me a joke"}]

response = client.responses.create(model="gpt-4o-mini", input=history, store=False)

print(response.output_text)

# Add the response to the conversation
history += [
    {"role": output.role, "content": output.content} for output in response.output
]

history.append({"role": "user", "content": "tell me another"})

second_response = client.responses.create(
    model="gpt-4o-mini", input=history, store=False
)

print(second_response.output_text)


# OpenAI APIs for conversation state default is true
#


response = client.responses.create(
    model="gpt-4o-mini",
    input="tell me a joke",
)
print(response.output_text)

#here history is not send still it is able to maintain the conversation state using previous response id 

response2 = client.responses.create(
    model="gpt-4o-mini",
    previous_response_id=response.id,
    input=[{"role": "user", "content": "explain why this is funny."}],
)
print(response2.output_text)
