from datetime import datetime
import uuid

class SharedState:
    def __init__(self):
        self.state = {
            "patient_id": str(uuid.uuid4()),
            "input_text": "",
            "clean_input": "",
            "intake_report": "",
            "research": {},
            "risk_level": "LOW",
            "emergency_action": "",
            "agent_logs": [],
            "icd_case": None,
            "timestamp": str(datetime.now())
        }

    def update(self, key, value):
        self.state[key] = value

    def log(self, message):
        self.state["agent_logs"].append({
            "time": str(datetime.now()),
            "message": message
        })

    def get_state(self):
        return self.state