#Final app.py 
#import files

from flask import Flask, render_template, request
from openai import OpenAI
from flask_cors import CORS
import os
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT_V1

app = Flask(__name__)
CORS(app)

load_dotenv()
api_key = os.getenv('API_KEY')


client = OpenAI(api_key = api_key)

def get_completion(query, model="gpt-4o-mini"):
    system_prompt = SYSTEM_PROMPT_V1
    user_prompt = f"Q: {query}"

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
    userText = request.args.get('msg')  
    response = get_completion(userText)  
    #return str(bot.get_response(userText)) 
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Default to port 5000 locally
    app.run(host='0.0.0.0', port=port)


