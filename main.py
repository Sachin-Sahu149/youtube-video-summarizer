from fastapi import FastAPI
import os
from dotenv import load_dotenv
from google import generativeai


load_dotenv()

app = FastAPI()


@app.get('/')
def root():
    return {"Message":"Welcome back"}


@app.get("/summary")
async def get_summary():
    # make an api call to gemini to check its working
    a = 5


apikey = os.getenv('GOOGLE_GEMINI_API')

print("Hellow Sachin! :: ",apikey)



client = generativeai.Client(apikey)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)