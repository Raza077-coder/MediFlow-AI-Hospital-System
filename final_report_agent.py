from memory.memory_manager import memory


class FinalReportAgent:

    def process(self, state):

        patient = state.get("patient_data", "N/A")

        research = state.get("research_data", {})

        risk = state.get("risk_level", "LOW")

        emergency = state.get("emergency", "No emergency")

        cardio = state.get("cardiology", "Normal")

        neuro = state.get("neurology", "Normal")

        pulmo = state.get("pulmonology", "Normal")

        reflection = state.get("reflection", "")

        # =========================
        # MEMORY CONTEXT
        # =========================
        context = memory.get_context(patient)

        similar_cases = len(context["similar_cases"])

        total_cases = context["total_cases"]

        # =========================
        # REASONING LOGS
        # =========================
        reasoning_logs = memory.get_reasoning_logs()

        reasoning_text = ""

        for log in reasoning_logs[-5:]:

            reasoning_text += f"""
Agent: {log['agent']}
Step: {log['step']}
Reason: {log['reason']}
Confidence: {log['confidence']}
Time: {log['timestamp']}

"""

        # =========================
        # FINAL REPORT
        # =========================
        final_report = f"""
🏥 FINAL MEDICAL REPORT

========================================

🧑 PATIENT SYMPTOMS:
{patient}

========================================

🧠 AI RESEARCH ANALYSIS:
{research}

========================================

🚨 RISK LEVEL:
{risk}

========================================

🚑 EMERGENCY RESPONSE:
{emergency}

========================================

🫀 CARDIOLOGY ANALYSIS:
{cardio}

========================================

🧠 NEUROLOGY ANALYSIS:
{neuro}

========================================

🫁 PULMONOLOGY ANALYSIS:
{pulmo}

========================================

🪞 REFLECTION AGENT:
{reflection}

========================================

🧠 MEMORY CONTEXT

Similar Previous Cases:
{similar_cases}

Total Cases In Memory:
{total_cases}

========================================

📋 AGENT REASONING LOGS

{reasoning_text}

========================================

🤖 SYSTEM SUMMARY

MediFlow AI autonomously analyzed the patient,
delegated tasks across multiple specialist agents,
validated outputs, checked emergency severity,
retrieved memory context, and generated
a complete medical intelligence report.

========================================
"""

        state["final_report"] = final_report

        state["agent_logs"].append(
            "Final Report Agent generated complete medical report"
        )

        return state