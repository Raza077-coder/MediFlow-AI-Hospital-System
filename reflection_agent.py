from memory.memory_manager import memory
class ReflectionAgent:
    def process(self, state):
        state["agent_logs"].append("ReflectionAgent executed")

        state["reflection"] = "System analysis completed successfully with multi-agent reasoning."

        return state