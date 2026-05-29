medical_db = [
    {
        "condition": "Myocardial Infarction",
        "symptoms": [
            "chest pain",
            "sweating",
            "dizziness",
            "breathing difficulty"
        ],
        "risk": "CRITICAL"
    },

    {
        "condition": "Pneumonia",
        "symptoms": [
            "fever",
            "cough",
            "breathing difficulty"
        ],
        "risk": "HIGH"
    },

    {
        "condition": "Stroke",
        "symptoms": [
            "slurred speech",
            "weakness",
            "confusion"
        ],
        "risk": "CRITICAL"
    }
]


def query_rag(symptoms):

    symptoms = symptoms.lower()

    matches = []

    for disease in medical_db:

        score = 0

        for keyword in disease["symptoms"]:

            if keyword in symptoms:
                score += 1

        if score > 0:

            matches.append({
                "condition": disease["condition"],
                "risk": disease["risk"],
                "score": score
            })

    # sort by highest match
    matches = sorted(
        matches,
        key=lambda x: x["score"],
        reverse=True
    )

    # determine overall risk
    risk_level = "LOW"

    for m in matches:

        if m["risk"] == "CRITICAL":
            risk_level = "CRITICAL"
            break

        elif m["risk"] == "HIGH":
            risk_level = "HIGH"

    return {
        "matches": matches,
        "risk_level": risk_level
    }