# workflows/hospital_workflow.py

# ==========================================
# MEDIFLOW AI — HOSPITAL WORKFLOW ENGINE
# ==========================================

from memory.memory_manager import memory


# ==========================================
# MAIN WORKFLOW
# ==========================================

def run_workflow(state):

    # ==========================================
    # INPUT
    # ==========================================

    text = state.get(
        "patient_data",
        ""
    ).strip().lower()

    # ==========================================
    # CLEAN INPUT
    # ==========================================

    clean_input = text

    # ==========================================
    # AGENT LOGS
    # ==========================================

    agent_logs = []

    agent_logs.append(
        "Manager Agent started workflow"
    )

    # ==========================================
    # RISK DETECTION
    # ==========================================

    critical_keywords = [
        "chest pain",
        "stroke",
        "breathing",
        "breathing difficulty",
        "slurred speech",
        "confusion",
        "weakness",
        "heart attack",
        "unconscious",
        "severe headache",
        "covid",
        "fever"
    ]

    high_keywords = [
        "dizziness",
        "cough",
        "infection",
        "fatigue"
    ]

    if any(k in text for k in critical_keywords):

        risk = "CRITICAL"

    elif any(k in text for k in high_keywords):

        risk = "HIGH"

    else:

        risk = "LOW"

    agent_logs.append(
        f"Risk level detected: {risk}"
    )

    # ==========================================
    # RESEARCH AGENT (SIMULATED RAG)
    # ==========================================

    matches = []

    if "chest pain" in text:

        matches.append({
            "condition": "Myocardial Infarction",
            "risk": "CRITICAL",
            "score": 4
        })

    if "slurred speech" in text:

        matches.append({
            "condition": "Stroke",
            "risk": "CRITICAL",
            "score": 4
        })

    if "breathing" in text or "covid" in text:

        matches.append({
            "condition": "Respiratory Distress",
            "risk": "CRITICAL",
            "score": 3
        })

    if "fever" in text:

        matches.append({
            "condition": "Severe Infection",
            "risk": "HIGH",
            "score": 2
        })

    # ==========================================
    # FALLBACK CONDITION
    # ==========================================

    if not matches:

        matches.append({
            "condition": "General Condition",
            "risk": "LOW",
            "score": 1
        })

    research = {
        "matches": matches,
        "risk_level": risk
    }

    agent_logs.append(
        "Research Agent completed disease matching"
    )

    # ==========================================
    # SPECIALIST AGENTS
    # ==========================================

    # CARDIOLOGY
    if "chest pain" in text:

        cardiology = "Possible Acute Coronary Syndrome (ACS)"

    else:

        cardiology = "No major cardiac issue detected."

    # NEUROLOGY
    if "slurred speech" in text or "confusion" in text:

        neurology = "Stroke suspected"

    else:

        neurology = "Normal"

    # PULMONOLOGY
    if "breathing" in text or "covid" in text:

        pulmonology = "Respiratory risk"

    else:

        pulmonology = "Normal"

    agent_logs.append(
        "Specialist Agents completed analysis"
    )

    # ==========================================
    # EMERGENCY AGENT
    # ==========================================

    if risk == "CRITICAL":

        emergency_action = (
            "🚨 CALL AMBULANCE + ICU REFERRAL"
        )

    elif risk == "HIGH":

        emergency_action = (
            "⚠ URGENT HOSPITAL VISIT REQUIRED"
        )

    else:

        emergency_action = (
            "✅ MONITOR PATIENT"
        )

    agent_logs.append(
        "Emergency Agent completed triage"
    )

    # ==========================================
    # LLM ANALYSIS
    # ==========================================

    llm_analysis = f"""
Possible Conditions:

Patient symptoms: {text}

Risk Level: {risk}

Recommended Action:

Emergency Department if critical
Standard monitoring if low risk
"""

    # ==========================================
    # MEMORY STORAGE
    # ==========================================

    memory.add_case({
        "patient": text,
        "risk": risk,
        "emergency": emergency_action
    })

    agent_logs.append(
        "Memory Manager stored patient case"
    )

    # ==========================================
    # FINAL REPORT AGENT
    # ==========================================

    final_report = f"""
🏥 FINAL MEDICAL REPORT

PATIENT:
{text}

🧠 RESEARCH:
{research}

🚨 EMERGENCY:
{emergency_action}

🫀 CARDIOLOGY:
{cardiology}

🧠 NEUROLOGY:
{neurology}

🫁 PULMONOLOGY:
{pulmonology}

📊 FINAL RISK:
{risk}
"""

    agent_logs.append(
        "Final Report Agent generated report"
    )

    # ==========================================
    # FINAL STATE
    # ==========================================

    final_state = {
        "patient_data": state.get(
            "patient_data"
        ),

        "clean_input": clean_input,

        "risk_level": risk,

        "research": research,

        "llm_analysis": llm_analysis,

        "cardiology_report": cardiology,

        "neurology_report": neurology,

        "pulmonology_report": pulmonology,

        "emergency_action": emergency_action,

        "final_report": final_report,

        "agent_logs": agent_logs
    }

    # ==========================================
    # RETURN
    # ==========================================

    return final_state