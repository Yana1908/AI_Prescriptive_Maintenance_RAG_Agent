import requests

url = "http://127.0.0.1:8000/alert"

payload = {
    "machine_id": "PUMP-01",
    "error_code": "E-404",
    "temperature": 105
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())