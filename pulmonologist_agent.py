from memory.memory_manager import memory
class PulmonologistAgent:
    def process(self, state):
        state["agent_logs"].append("PulmonologistAgent executed")

        text = state.get("clean_input", "")

        if "breathing difficulty" in text:
            state["pulmonology_report"] = "Possible respiratory distress. Oxygen therapy recommended."
        else:
            state["pulmonology_report"] = "No major pulmonary issue detected."

        return state