from fastapi import FastAPI
from app.graph.workflow import app as graph_app
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI System Online"}

@app.post("/chat")
async def chat(question: str):
    inputs = {"question": question}
    result = graph_app.invoke(inputs)
    return result["generation"]