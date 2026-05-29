import sqlite3
import pandas as pd
from database.config import DB_PATH

def get_icu_patients():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT 
        id,
        symptoms,
        risk_level,
        emergency_action,
        created_at
    FROM patient_logs
    WHERE risk_level = 'CRITICAL'
    ORDER BY created_at DESC
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df