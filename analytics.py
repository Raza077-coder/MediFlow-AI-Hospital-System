import sqlite3


def get_risk_analytics():

    conn = sqlite3.connect("database/medical_logs.db")

    cursor = conn.cursor()

    cursor.execute("""

    SELECT risk_level, COUNT(*)

    FROM patient_logs

    GROUP BY risk_level

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows