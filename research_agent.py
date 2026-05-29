import ollama
from memory.memory_manager import memory


class ResearchAgent:

    def process(self, state):

        symptoms = state.get("clean_input", "")

        # =========================
        # GET MEMORY CONTEXT
        # =========================
        context = memory.get_context(symptoms)

        # =========================
        # OLLAMA PROMPT
        # =========================
        prompt = f"""
You are a hospital medical AI.

Analyze patient symptoms carefully.

PATIENT:
{symptoms}

Return response in this format:

Condition:
Risk:
Reasoning:
Department:
"""

        try:

            response = ollama.chat(
                model="llama3.2:1b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            ai_output = response["message"]["content"]

            # =========================
            # SAVE AI OUTPUT
            # =========================
            state["research"] = ai_output

            # =========================
            # DETECT RISK
            # =========================
            lower = ai_output.lower()

            if "critical" in lower:
                state["risk_level"] = "CRITICAL"

            elif "high" in lower:
                state["risk_level"] = "HIGH"

            elif "medium" in lower:
                state["risk_level"] = "MEDIUM"

            else:
                state["risk_level"] = "LOW"

            # =========================
            # MEMORY REASONING
            # =========================
            memory.add_reasoning(
                agent="research_agent",
                step="ai_medical_analysis",
                reason=f"AI analyzed symptoms: {symptoms}",
                confidence=0.92
            )

            # =========================
            # LOGGING
            # =========================
            state["agent_logs"].append(
                "Research Agent completed Ollama analysis"
            )

        except Exception as e:

            state["research"] = f"Ollama Error: {str(e)}"

            state["risk_level"] = "MEDIUM"

            state["agent_logs"].append(
                "Research Agent failed"
            )

        return state

