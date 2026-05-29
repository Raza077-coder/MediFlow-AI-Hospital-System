from workflows.hospital_workflow import run_workflow
from memory.memory_manager import memory
from datetime import datetime


class ManagerAgent:
    """
    🧭 Controls full hospital AI workflow
    """

    def process(self, state: dict):

        # =========================
        # STEP 1 — START LOGGING
        # =========================
        memory.add_reasoning(
            agent="manager_agent",
            step="workflow_start",
            reason="Workflow initiated by user input",
            confidence=1.0
        )

        # =========================
        # STEP 2 — RUN MAIN WORKFLOW
        # =========================
        result = run_workflow(state)

        # =========================
        # STEP 3 — STORE MEMORY
        # =========================
        memory.add_memory({
            "patient_data": state.get("patient_data"),
            "risk": result.get("risk_level"),
            "emergency": result.get("emergency_action")
        })

        # =========================
        # STEP 4 — FINAL LOG
        # =========================
        memory.add_reasoning(
            agent="manager_agent",
            step="workflow_end",
            reason=f"Completed with risk {result.get('risk_level')}",
            confidence=0.95
        )

        return result