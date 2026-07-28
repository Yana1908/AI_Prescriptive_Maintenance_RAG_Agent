from fastapi import FastAPI
from pydantic import BaseModel

from backend.query_generator import generate_query

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


# Receive IoT Alert
@app.post("/alert")
def receive_alert(alert: IoTAlert):

    # Convert alert to dictionary
    alert_data = {
        "machine_id": alert.machine_id,
        "error_code": alert.error_code,
        "temperature": alert.temperature
    }

    # Generate search query
    query = generate_query(alert_data)

    return {
        "status": "Alert received successfully",
        "alert": alert_data,
        "generated_query": query
    }