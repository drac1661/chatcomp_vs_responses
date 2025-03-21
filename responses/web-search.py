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



# Basic web search with tool web_search_preview 


response = client.responses.create(
    model="gpt-4o",
    tools=[
        {
            "type": "web_search_preview",
        }
    ],
    input="What are the best restaurants around adyar chennai?",
)

print(response.output_text)


# Basic web search with location


response = client.responses.create(
    model="gpt-4o",
    tools=[
        {
            "type": "web_search_preview",
            "user_location": {
                "type": "approximate",
                "country": "IN",
                "city": "Ranchi",
            },
        }
    ],
    input="What are the best restaurants around dhurwa dam?",
)

print(response.output_text)
response.output[1].content[0].annotations
response.output[1].content[0].annotations[0].url
