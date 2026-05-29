from typing import TypedDict, Dict, Any

class MedicalState(TypedDict, total=False):
    patient_data: str
    clean_input: str
    intake_report: str
    research: Dict[str, Any]
    cardiology_report: str
    pulmonology_report: str
    neurology_report: str
    emergency_action: str
    validation: str
    risk_level: str
    final_report: str