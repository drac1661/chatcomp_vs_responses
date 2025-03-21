import requests
import json
import os
from dotenv import load_dotenv
from flask import request, Flask, jsonify

from flask_cors import CORS

load_dotenv()
api_key = os.getenv("api_key")
hostchat = os.getenv("hostchat")
hostresponse = os.getenv("hostresponse")

app = Flask(__name__)
CORS(app)


@app.route("/responses", methods=["POST"])
def get_response():
    prompt = request.json["prompt"]
    url = hostresponse
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    model = "gpt-4o-mini"
    input = prompt
    response = requests.post(
        hostresponse, headers=headers, json={"model": model, "input": input}
    )
    response_json = response.json()
    # with open("responses.json", "w") as outfile:
    #     json.dump(response_json, outfile)
    return jsonify({"message": response_json["output"][0]["content"][0]["text"]})


@app.route("/chat_completion", methods=["POST"])
def get_chat_completion():
    prompt = request.json["prompt"]
    url = hostchat
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": ""},
            {"role": "user", "content": prompt},
        ],
    }
    response = requests.post(hostchat, headers=headers, json=data)
    response_json = response.json()
    # with open("chat_completion.json", "w") as outfile:
    #     json.dump(response_json, outfile)
    return jsonify({"message": response_json["choices"][0]["message"]["content"]})


if __name__ == "__main__":
    app.run(debug=False)
