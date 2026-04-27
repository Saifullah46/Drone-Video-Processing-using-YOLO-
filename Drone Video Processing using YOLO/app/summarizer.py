def generate_summary(counts):
    if not counts:
        return "No significant objects detected. The field looks empty."

    parts = [f"{v} {k}" for k, v in counts.items()]
    object_text = ", ".join(parts)

    if "cow" in counts or "goat" in counts:
        insight = "Livestock activity observed in the field."
    elif "car" in counts or "truck" in counts:
        insight = "Vehicle movement detected."
    elif "person" in counts:
        insight = "Human activity detected."
    else:
        insight = "General activity observed."

    return f"{object_text} detected. {insight}"
