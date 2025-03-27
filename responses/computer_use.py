from openai import OpenAI
import openai
import os
from dotenv import load_dotenv

openai.api_base = os.getenv("base_url")
openai.api_key = os.getenv("OPENAI_API_KEY")

load_dotenv()


import base64


def image_to_base64(image_path):
    print("a")
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode("utf-8")
        # print(base64_string)
    return base64_string


# Example usage
image_path = r"C:\Users\e430275.SPI-GLOBAL\Desktop\openwebui\chatcomp_vs_responses\images\Screenshot(24).png"


client = OpenAI(
    base_url=os.getenv("base_url"),
    api_key=os.getenv("OPENAI_API_KEY"),
)


response = client.responses.create(
    model="computer-use-preview",
    tools=[
        {
            "type": "computer_use_preview",
            "display_width": 1024,
            "display_height": 768,
            "environment": "browser",  # other possible values: "mac", "windows", "ubuntu"
        }
    ],
    input=[
        {"role": "user", "content": "Check the weather of today according to Aaj Tak."},
        # {
        #     "type": "input_image",
        #     "image_url": f"data:image/png;base64,{image_to_base64(image_path)}"  # This includes the image
        # }
    ],
    reasoning={
        "generate_summary": "concise",
    },
    truncation="auto",
)

print(response.output)
print(response.output[0].call_id)
# print(computer_call.id)

# ------------------------------------------------------------------------

response1 = client.responses.create(
    model="computer-use-preview",
    previous_response_id=response.id,
    tools=[
        {
            "type": "computer_use_preview",
            "display_width": 1024,
            "display_height": 768,
            "environment": "browser",
        }
    ],
    input=[
        {
            "call_id": response.output[0].call_id,
            "type": "computer_call_output",
            "output": {
                "type": "input_image",
                "image_url": f"data:image/png;base64,{image_to_base64(image_path)}",
            },
        }
    ],
    truncation="auto",
)

print(response1.output)

image_path1 = r"C:\Users\e430275.SPI-GLOBAL\Desktop\openwebui\chatcomp_vs_responses\images\Screenshot(25).png"

response2 = client.responses.create(
    model="computer-use-preview",
    previous_response_id=response1.id,
    tools=[
        {
            "type": "computer_use_preview",
            "display_width": 1024,
            "display_height": 768,
            "environment": "browser",
        }
    ],
    input=[
        {
            "call_id": response1.output[1].call_id,
            "type": "computer_call_output",
            "output": {
                "type": "input_image",
                "image_url": f"data:image/png;base64,{image_to_base64(image_path1)}",
            },
        }
    ],
    truncation="auto",
)

print(response2.output)


# ------------------------------------------------------------------------

image_path2 = r"C:\Users\e430275.SPI-GLOBAL\Desktop\openwebui\chatcomp_vs_responses\images\Screenshot(26).png"

response3 = client.responses.create(
    model="computer-use-preview",
    previous_response_id=response2.id,
    tools=[
        {
            "type": "computer_use_preview",
            "display_width": 1024,
            "display_height": 768,
            "environment": "browser",
        }
    ],
    input=[
        {
            "call_id": response2.output[0].call_id,
            "type": "computer_call_output",
            "output": {
                "type": "input_image",
                "image_url": f"data:image/png;base64,{image_to_base64(image_path2)}",
            },
        }
    ],
    truncation="auto",
)

print(response3.output)
