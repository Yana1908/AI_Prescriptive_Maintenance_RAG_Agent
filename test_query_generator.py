from backend.query_generator import generate_query

alert = {
    "machine_id": "PUMP-01",
    "error_code": "E-404",
    "temperature": 105
}

query = generate_query(alert)

print(query)