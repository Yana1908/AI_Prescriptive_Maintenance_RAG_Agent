def generate_recommendation(results):

    if not results:
        return "No relevant maintenance information found."

    recommendation = (
        "Recommended Maintenance Action:\n\n"
        + results[0]["text"][:500]
    )

    return recommendation