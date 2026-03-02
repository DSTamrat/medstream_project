import os
import random
import pandas as pd
from datetime import datetime, timedelta

BASE = r"C:\Users\PC\OneDrive\Desktop\medstream_project"
random.seed(42)

N_PATIENTS = 400
N_ENCOUNTERS = 1000
N_NOTES = 50  # balanced-ish across 3 classes

genders = ["M", "F"]
primary_conditions = [
    ("I50.9", "Heart failure"),
    ("E11.9", "Type 2 diabetes"),
    ("I10", "Hypertension"),
    ("J45.909", "Asthma"),
    ("N18.3", "CKD stage 3"),
    ("I25.10", "Coronary artery disease"),
    ("J44.9", "COPD"),
]

comorbidity_pool = [
    "Hypertension",
    "Hyperlipidemia",
    "Obesity",
    "CKD",
    "CAD",
    "COPD",
    "Depression",
    "Anxiety",
    "Atrial fibrillation",
]

encounter_types = ["ED", "Inpatient", "Outpatient"]

def random_date(start_date, end_date):
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))

def generate_patients():
    patients = []
    for i in range(1, N_PATIENTS + 1):
        pid = f"P{i:04d}"
        age = random.randint(25, 90)
        gender = random.choice(genders)
        icd, cond = random.choice(primary_conditions)

        n_comorbid = random.randint(0, 3)
        comorbs = random.sample(comorbidity_pool, n_comorbid)
        comorbs_str = ", ".join(comorbs) if comorbs else ""

        patients.append(
            {
                "patient_id": pid,
                "age": age,
                "gender": gender,
                "primary_condition_code": icd,
                "primary_condition": cond,
                "comorbidities": comorbs_str,
            }
        )
    return pd.DataFrame(patients)

def severity_score(row):
    score = 0
    cond = row["primary_condition"]
    comorbs = row["comorbidities"]

    if cond in ["Heart failure", "CKD stage 3", "COPD", "Coronary artery disease"]:
        score += 2
    if "CKD" in comorbs or "CAD" in comorbs or "COPD" in comorbs:
        score += 1
    if "Obesity" in comorbs or "Hyperlipidemia" in comorbs:
        score += 0.5
    if row["age"] >= 75:
        score += 1
    return score

def generate_encounters(patients_df):
    encounters = []
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2025, 1, 1)

    for i in range(1, N_ENCOUNTERS + 1):
        eid = f"E{i:05d}"
        patient = patients_df.sample(1).iloc[0]
        pid = patient["patient_id"]
        sev = severity_score(patient)

        etype = random.choices(
            encounter_types,
            weights=[0.2, 0.3, 0.5],
            k=1
        )[0]

        if etype == "Outpatient":
            los = 0
        elif etype == "ED":
            los = random.choice([0, 0, 1])
        else:
            if sev >= 3:
                los = random.randint(5, 12)
            elif sev >= 2:
                los = random.randint(3, 8)
            else:
                los = random.randint(1, 5)

        base_prob = 0.05
        if sev >= 3:
            base_prob += 0.25
        elif sev >= 2:
            base_prob += 0.15
        if etype == "Inpatient":
            base_prob += 0.1

        readmitted = "Yes" if random.random() < base_prob else "No"

        edate = random_date(start_date, end_date)

        encounters.append(
            {
                "encounter_id": eid,
                "patient_id": pid,
                "encounter_date": edate.strftime("%Y-%m-%d"),
                "encounter_type": etype,
                "los_days": los,
                "readmitted_30d": readmitted,
            }
        )
    return pd.DataFrame(encounters)

high_risk_templates = [
    "Patient with worsening {cond}, presenting with {symptom1} and {symptom2}. High concern for decompensation, requires urgent management.",
    "Severe exacerbation of {cond}. {symptom1} noted, with {symptom2}. Close monitoring and possible ICU transfer.",
    "{cond} with acute deterioration. {symptom1}, {symptom2}, and poor response to home medications.",
]

medium_risk_templates = [
    "Chronic {cond}, currently stable but with recent {symptom1}. Recommend close follow-up and medication adjustment.",
    "{cond} with moderate symptoms including {symptom1}. No acute distress, but risk of worsening without adherence.",
    "Ongoing management of {cond}. {symptom1} present, labs borderline. Follow-up scheduled.",
]

low_risk_templates = [
    "{cond} well controlled. No {symptom1}, no {symptom2}. Routine follow-up visit.",
    "Stable {cond}. Patient denies {symptom1}. Medications tolerated, no recent exacerbations.",
    "Follow-up for {cond}. No acute complaints, exam unremarkable.",
]

symptoms_pool = [
    "shortness of breath",
    "chest pain",
    "leg swelling",
    "fatigue",
    "dizziness",
    "cough",
    "wheezing",
    "headache",
    "palpitations",
]

def generate_clinical_notes(encounters_df, patients_df):
    notes = []
    labels = ["high_risk"] * 17 + ["medium_risk"] * 17 + ["low_risk"] * 16
    random.shuffle(labels)

    sampled_encounters = encounters_df.sample(N_NOTES, random_state=42)

    for i, (idx, enc) in enumerate(sampled_encounters.iterrows()):
        nid = f"N{i+1:04d}"
        eid = enc["encounter_id"]
        pid = enc["patient_id"]
        patient = patients_df[patients_df["patient_id"] == pid].iloc[0]
        cond = patient["primary_condition"]

        label = labels[i]
        s1, s2 = random.sample(symptoms_pool, 2)

        if label == "high_risk":
            template = random.choice(high_risk_templates)
        elif label == "medium_risk":
            template = random.choice(medium_risk_templates)
        else:
            template = random.choice(low_risk_templates)

        text = template.format(cond=cond, symptom1=s1, symptom2=s2)

        notes.append(
            {
                "note_id": nid,
                "encounter_id": eid,
                "patient_id": pid,
                "note_text": text,
                "label": label,
            }
        )
    return pd.DataFrame(notes)

def main():
    os.makedirs(os.path.join(BASE, "data"), exist_ok=True)

    patients_df = generate_patients()
    encounters_df = generate_encounters(patients_df)
    notes_df = generate_clinical_notes(encounters_df, patients_df)

    patients_df.to_csv(os.path.join(BASE, "data", "patients.csv"), index=False)
    encounters_df.to_csv(os.path.join(BASE, "data", "encounters.csv"), index=False)
    notes_df.to_csv(os.path.join(BASE, "data", "clinical_notes.csv"), index=False)

    print("Synthetic patients, encounters, and clinical notes generated.")

if __name__ == "__main__":
    main()
