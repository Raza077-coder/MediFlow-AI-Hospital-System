from memory.memory_manager import memory
class CardiologistAgent:
    def process(self, state):
        state["agent_logs"].append("CardiologistAgent executed")

        text = state.get("clean_input", "")

        if "chest pain" in text:
            state["cardiology_report"] = "Possible Acute Coronary Syndrome (ACS). Immediate ECG recommended."
        else:
            state["cardiology_report"] = "No major cardiac issue detected."

        return state