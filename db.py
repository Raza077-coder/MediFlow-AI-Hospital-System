import sqlite3
import json
from datetime import datetime

DB_NAME = "database.db"


# =========================
# INIT DATABASE
# =========================
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symptoms TEXT,
        risk TEXT,
        emergency TEXT,
        research TEXT,
        final_report TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully")


# =========================
# SAVE CASE (MAIN LOGGER)
# =========================
def save_case(result: dict):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    symptoms = result.get("patient_data", "Unknown")
    risk = result.get("risk_level", "UNKNOWN")
    emergency = result.get("emergency_action", "N/A")

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


# =========================
# GET ALL CASES
# =========================
def get_all_cases(limit=50):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM cases
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cur.fetchall()
    conn.close()

    return rows


# =========================
# CLEAR HISTORY
# =========================
def clear_cases():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("DELETE FROM cases")

    conn.commit()
    conn.close()


# =========================
# ICU STATS
# =========================
def get_icu_stats():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        SELECT risk, COUNT(*)
        FROM cases
        GROUP BY risk
    """)

    data = cur.fetchall()
    conn.close()

    return data