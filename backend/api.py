from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Structure of IoT Alert
class IoTAlert(BaseModel):
    machine_id: str
    error_code: str
    temperature: float

# POST API
@app.post("/iot-alert")
def receive_alert(alert: IoTAlert):

    print("Received IoT Alert")
    print("Machine ID:", alert.machine_id)
    print("Error Code:", alert.error_code)
    print("Temperature:", alert.temperature)

    return {
        "status": "Alert Received Successfully",
        "machine_id": alert.machine_id,
        "error_code": alert.error_code,
        "temperature": alert.temperature
    }