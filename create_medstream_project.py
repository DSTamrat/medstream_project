import os
import pandas as pd

BASE = r"C:\Users\PC\OneDrive\Desktop\medstream_project"

folders = [
    BASE,
    os.path.join(BASE, "data"),
    os.path.join(BASE, "notebooks"),
    os.path.join(BASE, "app"),
    os.path.join(BASE, "models"),
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

patients_df = pd.DataFrame([
    ["P001", 56, "F", "Type 2 Diabetes"],
    ["P002", 43, "M", "Hypertension"],
    ["P003", 70, "F", "CHF"],
    ["P004", 35, "M", "Asthma"],
    ["P005", 62, "F", "CKD"],
], columns=["patient_id", "age", "gender", "primary_condition"])

encounters_df = pd.DataFrame([
    ["E001", "P001", "2025-01-10", "Inpatient", 4, "Yes"],
    ["E002", "P002", "2025-01-12", "ED", 1, "No"],
    ["E003", "P003", "2025-01-15", "Inpatient", 7, "Yes"],
    ["E004", "P004", "2025-01-18", "Outpatient", 0, "No"],
    ["E005", "P005", "2025-01-20", "Inpatient", 5, "No"],
], columns=["encounter_id", "patient_id", "encounter_date", "encounter_type", "los_days", "readmitted_30d"])

clinical_notes_df = pd.DataFrame([
    ["N001", "E001", "P001", "Patient with poorly controlled diabetes, elevated HbA1c, needs medication adjustment and diet counseling.", "high_risk"],
    ["N002", "E002", "P002", "Mild hypertension, lifestyle modification advised, no acute distress.", "low_risk"],
    ["N003", "E003", "P003", "CHF exacerbation, shortness of breath, edema, requires close follow-up and medication optimization.", "high_risk"],
    ["N004", "E004", "P004", "Asthma well controlled, routine follow-up, no recent exacerbations.", "low_risk"],
    ["N005", "E005", "P005", "Chronic kidney disease stage 3, stable labs, monitor renal function regularly.", "medium_risk"],
], columns=["note_id", "encounter_id", "patient_id", "note_text", "label"])

patients_df.to_csv(os.path.join(BASE, "data", "patients.csv"), index=False)
encounters_df.to_csv(os.path.join(BASE, "data", "encounters.csv"), index=False)
clinical_notes_df.to_csv(os.path.join(BASE, "data", "clinical_notes.csv"), index=False)

with open(os.path.join(BASE, "notebooks", "placeholder.txt"), "w") as f:
    f.write("Jupyter notebooks go here.")

with open(os.path.join(BASE, "models", "placeholder.txt"), "w") as f:
    f.write("Trained models go here.")

with open(os.path.join(BASE, "app", "dashboard_app.py"), "w") as f:
    f.write("import streamlit as st\nst.title('MedStream Dashboard')")

with open(os.path.join(BASE, "README.md"), "w") as f:
    f.write("# MedStream Project\nSynthetic healthcare NLP pipeline.")

with open(os.path.join(BASE, "requirements.txt"), "w") as f:
    f.write("pandas\nnumpy\nscikit-learn\nnltk\nstreamlit\nplotly\njoblib")
