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


# IDEAS
# Bucket 1: Improving the Backend (BE) and core AI system
    # Grounding your AI system
        # Step 1: create a corpus of information about the office
        # Step 2: Connect that corpus of information to the LLM
            # Option 1: just stick the entire corpus of info into the prompt
            # Option 2 (probably too complicated/unnecessary for this use case) - RAG (retrieval augmented generation): create a separate index with each document being a question-answer pair.
    # Prompt engineering + Evaluation
        # Step 1: Try out different prompts with your FAQ
            # Step A: could also try out different AI models. Different OpenAI models + Anthropic models.
        # Step 2: Evaluate each of your prompts with an offline dataset
            # Step A: Manually create a groundtruth dataset with sample questions and answers (n=30)
            # Step B: Run the questions through your system and measure the accuracy
                # Step a: Manually label the correct/incorrect AI answers. Can use an Excel spreadsheet to label.
                # Step b: You could use an LLM to evaluate your system
    # Chat history logic
        # Step 1: you need to send back the entire chat history from the FE to the BE
            # Only want to send back the previous 5 chat turns
        # Step 2: pass back the previou questions and answers to the LLM
# Bucket 2: Improving the Frontend (FE)
    # Setting up a React app for FE. The React app will your BE endpoint.
    # Create a nicer user interface (color scheme, logo, polish) - online tutorials to build a chat app using React
    # Streaming tokens from the FE to the BE
# Bucket 3: Deploying your app
        # Deploy it as a separate website (linked from your mom's webpage) OR a widget depending on if you have access to make bigger changes
        # To deploy it, you can use Github / heroku / vercel\
    
# Goals
    # Goal 1: learn about full-stack development
    # Goal 2: build out your resume, can say you that you know how to build a product. You can talk about topics like prompt engienering, React, streaming, grounding AI systems, Python, etc.
    # Goal 3: ship your AI system to the website
