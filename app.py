#Final app.py 
#import files

from flask import Flask, render_template, request
from openai import OpenAI
from flask_cors import CORS
import os
import spacy

app = Flask(__name__)
CORS(app)

api_key  = "sk-HDNjLo-p5dHaLfucqro_pL8uDvagnLF9lJ9cX5eiNqT3BlbkFJS4nF--aCd1pfd7RiSVUAqgSaSEq4M5UUtBQrexvKgA"

client = OpenAI(api_key = api_key)

def get_completion(user_prompt, model="gpt-3.5-turbo"):
    system_prompt = """
    You are a helpful FAQ assistant for a doctor's office. Only respond to questions related to our business.

    Q: What are your business hours?
    A: Our business hours are 9 AM to 5 PM, Monday through Friday.

    Q: How can I contact customer service?
    A: You can contact customer service by emailing support@yourbusiness.com or calling (555) 555-5555.

    Q: {}
    A:""".format(user_prompt)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
        ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content

@app.route("/")
def home():    
    return render_template("index.html")

@app.route("/get")
def get_bot_response(): 
    print("get was called")   
    userText = request.args.get('msg')  
    print(userText)
    response = get_completion(userText)  
    #return str(bot.get_response(userText)) 
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Default to port 5000 locally
    app.run(host='0.0.0.0', port=port)


