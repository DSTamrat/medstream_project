import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import os

# Base path to your project
BASE = r"C:\Users\PC\OneDrive\Desktop\medstream_project"

# Load data
patients = pd.read_csv(os.path.join(BASE, "data", "patients.csv"))
encounters = pd.read_csv(os.path.join(BASE, "data", "encounters.csv"))
notes = pd.read_csv(os.path.join(BASE, "data", "clinical_notes.csv"))

# Load model + vectorizer
clf = joblib.load(os.path.join(BASE, "models", "note_classifier.pkl"))
vectorizer = joblib.load(os.path.join(BASE, "models", "vectorizer.pkl"))

# Streamlit page setup
st.set_page_config(page_title="MedStream NLP Dashboard", layout="wide")
st.title("MedStream NLP Dashboard")

# Top metrics
col1, col2, col3 = st.columns(3)
col1.metric("Patients", patients.shape[0])
col2.metric("Encounters", encounters.shape[0])
col3.metric("Clinical Notes", notes.shape[0])

st.markdown("---")

# Risk distribution chart
risk_counts = notes["label"].value_counts().reset_index()
risk_counts.columns = ["risk_label", "count"]

fig_risk = px.bar(
    risk_counts,
    x="risk_label",
    y="count",
    color="risk_label",
    title="Risk Distribution of Clinical Notes",
    text="count"
)
st.plotly_chart(fig_risk, use_container_width=True)

# LOS by risk
enc_notes = encounters.merge(notes, on=["encounter_id", "patient_id"], how="inner")

fig_los = px.box(
    enc_notes,
    x="label",
    y="los_days",
    color="label",
    title="Length of Stay by Risk Category"
)
st.plotly_chart(fig_los, use_container_width=True)

st.markdown("---")

# Prediction section
st.subheader("Predict Risk From a New Clinical Note")

user_note = st.text_area("Enter clinical note text:", height=150)

if st.button("Predict Risk"):
    if user_note.strip():
        vec = vectorizer.transform([user_note])
        pred = clf.predict(vec)[0]
        proba = clf.predict_proba(vec)[0]
        labels = clf.classes_

        st.success(f"Predicted Risk: {pred}")

        proba_df = pd.DataFrame({"risk_label": labels, "probability": proba})
        fig_proba = px.bar(
            proba_df,
            x="risk_label",
            y="probability",
            color="risk_label",
            title="Prediction Probabilities"
        )
        st.plotly_chart(fig_proba, use_container_width=True)
    else:
        st.warning("Please enter a clinical note.")
