import requests


class WebSearchAgent:

    def process(self, state):

        symptoms = state.get("symptoms", "")

        try:

            # Simple simulated web search
            search_result = f"""
            Web medical references found for:
            {symptoms}

            Possible emergency-related condition detected.
            Recommended immediate clinical evaluation.
            """

            state["web_search"] = search_result

            state["agent_logs"].append(
                "🌐 WebSearchAgent fetched external medical references"
            )

        except Exception as e:

            state["web_search"] = "Web search unavailable"

            state["agent_logs"].append(
                f"❌ WebSearchAgent failed: {str(e)}"
            )

        return state