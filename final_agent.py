from memory.memory_manager import memory
def final_agent(state):

    state["final_report"] = f"""
🏥 FINAL MEDICAL REPORT

PATIENT:
{state.get('patient_data','')}

------------------------
🧠 RESEARCH:
{state.get('research','')}

------------------------
🫀 CARDIOLOGY:
{state.get('cardiology_report','')}

------------------------
🚨 EMERGENCY:
{state.get('emergency_action','')}

------------------------
✅ VALIDATION:
{state.get('validation','')}
"""

    return state