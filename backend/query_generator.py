def generate_query(alert):

    machine = alert["machine_id"]
    error = alert["error_code"]
    temperature = alert["temperature"]

    query = (
        f"How to repair machine {machine} "
        f"with error code {error} "
        f"when temperature is {temperature}°C?"
    )

    return query


if __name__ == "__main__":

    sample_alert = {
        "machine_id": "PUMP-01",
        "error_code": "E-404",
        "temperature": 105
    }

    print(generate_query(sample_alert))