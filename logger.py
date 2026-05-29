import sqlite3
import json
from datetime import datetime

def save_case(result):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # extract safely
    symptoms = result.get("patient_data", "")
    risk = result.get("risk_level", "UNKNOWN")
    emergency = result.get("emergency_action", "N/A")

    # convert dict → string safely
    research = json.dumps(result.get("research", {}))
    final_report = result.get("final_report", "")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cur.execute("""
        INSERT INTO cases (
            symptoms,
            risk,
            emergency,
            research,
            final_report,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        str(symptoms),
        str(risk),
        str(emergency),
        research,
        final_report,
        timestamp
    ))

    conn.commit()
    conn.close()