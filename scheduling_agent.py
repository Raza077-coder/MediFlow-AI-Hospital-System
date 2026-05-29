from memory.memory_manager import memory
# agents/scheduling_agent.py

from langchain_ollama import ChatOllama
from utils.config import MODEL_NAME

llm = ChatOllama(
    model=MODEL_NAME
)


def scheduling_agent(state):

    emergency_result = state["emergency_result"]

    prompt = f"""
    You are a hospital scheduling agent.

    Based on:
    {emergency_result}

    Decide:
    - Appointment urgency
    - Recommended doctor type
    - Follow-up schedule
    - Hospital department

    Generate scheduling recommendations.
    """

    response = llm.invoke(prompt)

    return {
        "scheduling_result": response.content
    }