from memory.memory_manager import memory
class ValidationAgent:
    def process(self, state):
        state["agent_logs"].append("ValidationAgent executed")

        if state.get("risk_level") in ["CRITICAL", "HIGH"]:
            state["validation"] = "OK"
        else:
            state["validation"] = "OK"

        return state