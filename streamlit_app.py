import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database.db import init_db
from database.logger import save_case
from database.history import get_all_cases
from database.search import search_cases

from database.dashboard import (
    get_risk_distribution,
    get_emergency_trends,
    get_daily_traffic,
    get_doctor_performance
)

from workflows.hospital_workflow import run_workflow

# ✅ CREATE MEMORY INSTANCE HERE
from memory.memory_manager import memory


# ==========================
# INIT DATABASE
# ==========================

init_db()


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="MediFlow AI Hospital System",
    layout="wide"
)

st.title("🏥 MediFlow AI Hospital System")
st.write("Powered by LangGraph + Multi-Agent AI + LLM")


# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("🏥 MediFlow AI")

st.sidebar.info("""
AI-Powered Hospital Management System

Features:
- Multi-Agent AI
- Emergency Detection
- LLM Diagnosis
- Analytics Dashboard
- Patient History
- AI Medical Analysis
""")


# ==========================
# PATIENT INPUT
# ==========================

st.header("🩺 Patient Diagnosis")

patient_input = st.text_area(
    "Enter patient symptoms",
    placeholder="e.g. chest pain, fever, dizziness, breathing difficulty"
)


# ==========================
# ANALYZE BUTTON
# ==========================

if st.button("Analyze Patient"):

    if patient_input:

        with st.spinner("Running AI Hospital Workflow..."):

            state = {
                "patient_data": patient_input
            }

            result = run_workflow(state)

            save_case(result)
            memory.add_memory(result)

        st.success("Analysis Complete")


        # ==========================
        # FINAL REPORT
        # ==========================

        st.subheader("📋 Final Report")

        final_report = result.get("final_report", None)

        if final_report:
            st.write(final_report)
        else:
            st.error("No report generated")


        # ==========================
        # AI LLM ANALYSIS
        # ==========================

        st.subheader("🤖 AI Medical Analysis")

        st.write(
            result.get(
                "llm_analysis",
                "No AI analysis available"
            )
        )


        # ==========================
        # EMERGENCY
        # ==========================

        st.subheader("🚨 Emergency")

        st.error(
            result.get(
                "emergency_action",
                "No emergency detected"
            )
        )


        # ==========================
        # SPECIALISTS
        # ==========================

        cardio = result.get("cardiology_report")

        if cardio:

            st.subheader("🫀 Cardiology")

            st.write(cardio)


        pulmo = result.get("pulmonology_report")

        if pulmo:

            st.subheader("🫁 Pulmonology")

            st.write(pulmo)


        neuro = result.get("neurology_report")

        if neuro:

            st.subheader("🧠 Neurology")

            st.write(neuro)


        # ==========================
        # RESEARCH
        # ==========================

        st.subheader("🧠 RAG Research")

        st.json(
            result.get(
                "research",
                {}
            )
        )


        # ==========================
        # RISK LEVEL
        # ==========================

        st.subheader("🚨 Risk Level")

        risk = result.get("risk_level", "UNKNOWN")

        if risk == "CRITICAL":
            st.markdown(f"🔴 **{risk}**")
            st.error("Immediate medical attention required")

        elif risk == "HIGH":
            st.markdown(f"🟠 **{risk}**")
            st.warning("Monitor patient closely")

        else:
            st.markdown(f"🟢 **{risk}**")
            st.success("No immediate risk detected")


        # ==========================
        # DEBUG
        # ==========================

        with st.expander("⚙ Full AI State (Debug)"):

            st.json(result)


# ==========================
# SEARCH HISTORY
# ==========================

st.divider()

st.header("🔍 Search Patient History")

query = st.text_input(
    "Search symptoms"
)

if query:

    results = search_cases(query)

    if results:

        for r in results:

            st.markdown(f"""
            ### Case #{r[0]}

            **Symptoms:** {r[1]}

            **Risk:** {r[2]}

            **Emergency:** {r[3]}

            **Date:** {r[4]}
            """)

            st.divider()

    else:

        st.warning("No matching records found")


# ==========================
# PATIENT HISTORY
# ==========================

st.divider()

st.header("📁 Patient History")

history = get_all_cases()

if history:

    for h in history:

        st.markdown(f"""
        ### Case #{h[0]}

        **Symptoms:** {h[1]}

        **Risk:** {h[2]}

        **Emergency:** {h[3]}

        **Date:** {h[4]}
        """)

        st.divider()

else:

    st.info("No patient history available")


# ==========================
# ANALYTICS DASHBOARD
# ==========================

st.divider()

st.header("📊 Analytics Dashboard")


# ==========================
# LOAD ANALYTICS
# ==========================

risk_df = get_risk_distribution()

emergency_df = get_emergency_trends()

traffic_df = get_daily_traffic()

doctor_df = get_doctor_performance()


# ==========================
# PIE CHART
# ==========================

st.subheader("🥧 Risk Distribution")

if len(risk_df) > 0:

    fig, ax = plt.subplots()

    sizes = risk_df["total"].tolist()

    labels = risk_df["risk_level"].tolist()

    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%'
    )

    ax.axis("equal")

    st.pyplot(fig)

else:

    st.warning(
        "No risk analytics data available."
    )


# ==========================
# EMERGENCY TRENDS
# ==========================

st.subheader("🚨 Emergency Trends")

if not emergency_df.empty:

    st.line_chart(
        emergency_df.set_index("date")
    )

else:

    st.warning(
        "No emergency trend data"
    )


# ==========================
# DAILY TRAFFIC
# ==========================

st.subheader("🏥 Daily Hospital Traffic")

if not traffic_df.empty:

    st.area_chart(
        traffic_df.set_index("date")
    )

else:

    st.warning(
        "No hospital traffic data"
    )


# ==========================
# DOCTOR PERFORMANCE
# ==========================

st.subheader("👨‍⚕️ Doctor Performance Dashboard")

if doctor_df is not None and not doctor_df.empty:

    # SAFE COLUMN CHECK
    if "Doctor" in doctor_df.columns:
        chart_df = doctor_df.set_index("Doctor")
    else:
        chart_df = doctor_df.set_index(doctor_df.columns[0])

    st.dataframe(doctor_df)
    st.bar_chart(chart_df)

else:
    st.warning("No doctor performance data available")


# ==========================
# FOOTER
# ==========================

st.divider()

st.caption(
    "MediFlow AI • Multi-Agent Hospital Intelligence Platform"
)