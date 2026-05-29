from workflows.hospital_workflow import app

def run():
    print("🏥 MediFlow AI Running")

    text = input("Enter symptoms: ")

    state = {
        "patient_data": text
    }

    result = app.invoke(state)

    print("\n===== FINAL REPORT =====\n")
    print(result.get("final_report"))

    print("\nRISK:", result.get("risk_level"))


if __name__ == "__main__":
    run()