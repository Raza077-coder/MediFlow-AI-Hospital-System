from memory.memory_manager import memory
def process(self, state):

    symptoms = state["symptoms"]

    # 🔥 HERE (PASTE THIS)
    context = self.memory.get_context(symptoms)

    similar_cases = context["similar_cases"]
    recent = context["recent_cases"]

    # now your logic