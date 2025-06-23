import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Missing GOOGLE_API_KEY")

llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash")

while True:
    user_input=input("You: ")
    try:
        response=llm.invoke(user_input)
        print("Bot: ",response.content)
        print("-------------------------------------------------------")
    except Exception as e:
        print("Error: ",str(e))
        
 