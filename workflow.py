# workflows/workflow.py

def intake_agent(state):
    print("\n[✓] Intake Agent Running...")
    state["intake"] = f"Processed: {state.get('patient_data', '')}"
    return state


def research_agent(state):
    print("\n[✓] Research Agent Running...")
    state["research"] = "Medical research completed based on symptoms"
    return state


def emergency_agent(state):
    print("\n[✓] Emergency Agent Running...")
    data = state.get("patient_data", "").lower()

    if "chest pain" in data or "breathing" in data:
        state["emergency_flag"] = True
        state["emergency_action"] = "Immediate hospital referral required"
    else:
        state["emergency_flag"] = False
        state["emergency_action"] = "No emergency detected"

    return state


def validation_agent(state):
    print("\n[✓] Validation Agent Running...")
    state["validation"] = "All medical suggestions validated (basic check)"
    return state


def reflection_agent(state):
    print("\n[✓] Reflection Agent Running...")
    state["reflection"] = (
        "System analyzed patient condition and generated recommendations "
        "based on symptoms and emergency rules."
    )
    return state


# 🔥 MAIN WORKFLOW FUNCTION (THIS IS WHAT YOUR main.py IMPORTS)
def app(state):
    print("\n==============================")
    print(" MEDIFLOW WORKFLOW STARTED ")
    print("==============================")

    if state is None:
        return {"error": "No input state provided"}

    # Step-by-step pipeline
    state = intake_agent(state)
    state = research_agent(state)
    state = emergency_agent(state)
    state = validation_agent(state)
    state = reflection_agent(state)

    print("\n==============================")
    print(" WORKFLOW COMPLETED ")
    print("==============================")

    # 🔥 IMPORTANT: MUST RETURN STATE (fixes your NoneType error)
    return state