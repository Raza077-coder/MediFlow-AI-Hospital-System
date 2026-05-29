import ollama


def generate_medical_analysis(symptoms):

    prompt = f"""

You are MediFlow AI.

You are a hospital triage assistant.

You are NOT replacing doctors.

Your task is ONLY:
- emergency triage
- possible condition analysis
- department recommendation
- severity estimation

Never refuse.

Never say:
"I can't provide medical advice"

Always provide structured hospital triage analysis.

Patient Symptoms:
{symptoms}

Return EXACTLY in this format:

Possible Conditions:
-

Risk Level:
-

Recommended Department:
-

Immediate Actions:
-

Recommended Tests:
-

"""

    response = ollama.chat(

        model="llama3.2:1b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    return response["message"]["content"]