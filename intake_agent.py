from memory.memory_manager import memory
class IntakeAgent:
    def process(self, state):
        state["agent_logs"].append("Intake Agent executed")

        # yahan apni logic hogi
        text = state["input_text"]
        state["clean_input"] = text.lower().strip()

        return state