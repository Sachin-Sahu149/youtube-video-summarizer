import os
from dotenv import load_dotenv
from google import generativeai as genai

load_dotenv()

apikey = os.getenv('GOOGLE_GEMINI_API')

genai.configure(api_key=apikey)

def get_ai_response(prompt:str):
    
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text
    
prompt = "can you help me summarize youtube video, if yes then how can I accomplish this task"
print(get_ai_response(prompt))    


# main objective was to take create the system that fetches the transcript and summarize them later 
