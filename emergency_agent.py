from memory.memory_manager import memory
class EmergencyAgent:
    def process(self, state):
        state["agent_logs"].append("EmergencyAgent executed")

        risk = state.get("risk_level", "LOW")

        if risk == "CRITICAL":
            state["emergency_action"] = "🚨 CALL AMBULANCE + ICU REFERRAL"
        else:
            state["emergency_action"] = "Monitor Patient"

        return state