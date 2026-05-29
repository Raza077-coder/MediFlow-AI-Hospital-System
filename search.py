import sqlite3


def search_cases(query):

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

    WHERE symptoms LIKE ?

    ORDER BY id DESC

    """, (f"%{query}%",))

    rows = cursor.fetchall()

    conn.close()

    return rows