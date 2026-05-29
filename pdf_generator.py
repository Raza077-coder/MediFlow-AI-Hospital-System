from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(result, filename="medical_report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "MediFlow AI Medical Report",
        styles["Title"]
    )

    story.append(title)

    story.append(Spacer(1, 20))

    # PATIENT

    patient = Paragraph(
        f"<b>Patient Symptoms:</b><br/>{result.get('patient_data')}",
        styles["BodyText"]
    )

    story.append(patient)

    story.append(Spacer(1, 12))

    # RISK

    risk = Paragraph(
        f"<b>Risk Level:</b><br/>{result.get('risk_level')}",
        styles["BodyText"]
    )

    story.append(risk)

    story.append(Spacer(1, 12))

    # CARDIOLOGY

    cardio = Paragraph(
        f"<b>Cardiology Report:</b><br/>{result.get('cardiology_report')}",
        styles["BodyText"]
    )

    story.append(cardio)

    story.append(Spacer(1, 12))

    # EMERGENCY

    emergency = Paragraph(
        f"<b>Emergency Action:</b><br/>{result.get('emergency_action')}",
        styles["BodyText"]
    )

    story.append(emergency)

    story.append(Spacer(1, 12))

    # FINAL REPORT

    final_report = Paragraph(
        f"<b>Final Report:</b><br/>{result.get('final_report')}",
        styles["BodyText"]
    )

    story.append(final_report)

    doc.build(story)

    return filename