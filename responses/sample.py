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


response = client.responses.create(
    model="gpt-4o-mini", input="give name of 5 nation whose name start with A."
)
print(response.output_text)
response2 = client.responses.create(
    previous_response_id=response.id,
    model="gpt-4o-mini",
    input="give other 5 nation whose name start with A.",
)
print(response2.output_text)
response3 = client.responses.create(
    previous_response_id=response2.id,
    model="gpt-4o-mini",
    input="how many nation name you have given till now",
)
print(response3.output_text)


# using max tokens
response = client.responses.create(
    model="gpt-4o-mini",
    previous_response_id=response3.id,
    input="how many nation name you have given till now give names of them",
    max_output_tokens=17,
)
print(response.output_text)

response = client.responses.create(
    model="gpt-4o-mini",
    previous_response_id=response3.id,
    input="how many nation name you have given till now give names of them",
    max_output_tokens=100,
)
print(response.output_text)


# retrieving responses id
response = client.responses.retrieve(response3.id)
print(response.output_text)

#deleting responses
response = client.responses.del(response3.id)
print(response)


#input items

response = response = client.responses.input_items.list(response3.id)
print(response.data)

response = client.responses.input_items.list(response3.id,after=response.id)
print(response)