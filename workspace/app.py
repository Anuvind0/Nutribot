from flask import Flask, render_template, request, jsonify
import google.genai as genai
import sys
import json

app = Flask(__name__)
greet=["hi","hello","hey","thanks","thnx","thank you","goodbye","bye","good morning","good night"]
# Example chatbot function
def generate(prompt):
    client = genai.Client(api_key="AIzaSyAa5L6im7IW05I3fJRFGhsnDOVB-HVL1zk")
    response = client.models.generate_content(
    model="gemini-2.5-flash-lite", contents=prompt+" generate the answer in a one or two sentance regarding nutrition")
    print(type(response))
    y=response.text
    return y
def check(prompt):
    pt=f'"{prompt}"'
    client = genai.Client(api_key="AIzaSyAa5L6im7IW05I3fJRFGhsnDOVB-HVL1zk")
    response = client.models.generate_content(
    model="gemini-2.5-flash-lite", contents=pt+" can you check if this prompt is related to nutrition or nutrition related topics or food choices not,Just give me a single yes or no")
    print(response)
    y=response.text
    if y.lower().strip() == "yes":
        return generate(prompt)
    else:
        return "Sorry, I can only answer questions related to nutrition, diet, and food choices."
def chatbot_response(user_input):
    if user_input.lower().strip() in greet:
        return generate(user_input)
    else:
        return check(user_input)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_input = data.get("prompt", "")
    reply = chatbot_response(user_input)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
