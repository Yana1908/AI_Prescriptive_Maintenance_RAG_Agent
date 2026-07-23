from fastapi import FastAPI
from backend.query_generator import generate_query

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/alert")
def receive_alert(data: dict):

    query = generate_query(data)

    return {
        "status": "received",
        "search_query": query
    }