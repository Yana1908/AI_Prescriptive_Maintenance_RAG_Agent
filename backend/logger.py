from datetime import datetime


def save_log(alert, query, recommendation):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("outputs/logs.txt", "a", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write(f"Time : {current_time}\n")
        file.write(f"Machine : {alert['machine_id']}\n")
        file.write(f"Error Code : {alert['error_code']}\n")
        file.write(f"Temperature : {alert['temperature']}\n\n")

        file.write(f"Generated Query :\n{query}\n\n")

        file.write(f"Recommendation :\n{recommendation}\n")

        file.write("=" * 60 + "\n\n")