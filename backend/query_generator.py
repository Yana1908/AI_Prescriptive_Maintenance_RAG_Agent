def generate_query(alert):

    machine = alert["machine_id"]
    error = alert["error_code"]
    temperature = alert["temperature"]

    query = (
        f"How to troubleshoot error code {error} "
        f"for machine {machine} "
        f"when temperature is {temperature}?"
    )

    return query