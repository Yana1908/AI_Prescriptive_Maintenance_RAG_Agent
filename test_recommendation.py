from backend.recommendation import generate_recommendation

sample_results = [
    {
        "text": "Check the cooling fan. Inspect the motor wiring. Reset the controller after fixing the fault."
    }
]

print(generate_recommendation(sample_results))