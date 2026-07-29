from fastapi import FastAPI
from pydantic import BaseModel

from backend.query_generator import generate_query
from backend.retriever import search_manual
from backend.recommendation import generate_recommendation
from backend.logger import save_log

app = FastAPI()


# IoT Alert Model
class IoTAlert(BaseModel):
    machine_id: str
    error_code: str
    temperature: float


# Home Route
@app.get("/")
def home():
    return {
        "message": "AI Prescriptive Maintenance RAG Agent API is running"
    }


# Health Check
@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


# Receive IoT Alert
@app.post("/alert")
def receive_alert(alert: IoTAlert):

    # Convert alert object into dictionary
    alert_data = {
        "machine_id": alert.machine_id,
        "error_code": alert.error_code,
        "temperature": alert.temperature
    }

    # Generate search query
    query = generate_query(alert_data)

    # Search relevant manual chunks
    results = search_manual(query)

    # Generate maintenance recommendation
    recommendation = generate_recommendation(results)
    save_log(alert_data, query, recommendation)

    return {
        "status": "Success",
        "alert": alert_data,
        "generated_query": query,
        "recommendation": recommendation,
        "manual_results": results
    }