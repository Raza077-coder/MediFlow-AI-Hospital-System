import sqlite3


def get_all_cases():

    conn = sqlite3.connect("database/medical_logs.db")

    cursor = conn.cursor()

    cursor.execute("""

    SELECT
        id,
        symptoms,
        risk_level,
        emergency_action,
        created_at

    FROM patient_logs

    ORDER BY id DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows