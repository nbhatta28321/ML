import openai
import os
from dotenv import load_dotenv

load_dotenv() 
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set your API key
client = openai.OpenAI(api_key=OpenAI_Key)

def chatbot():
    print("Chatbot: Submit an article to summarize! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You  sumarize any article in just in few sentences."},
                {"role": "user", "content": user_input}
            ],
            temperature=0 
        )
        
        print("Chatbot:", response.choices[0].message.content.strip())      

# Run the chatbot
chatbot()
