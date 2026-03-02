#### **<p align="center">**

####   **<img src="https://via.placeholder.com/1200x250/0A2540/FFFFFF?text=MedStream%20-%20Clinical%20Risk%20NLP%20%26%20Analytics%20Dashboard" alt="MedStream Banner"/>**

#### **</p>**

#### &nbsp;    

* #### MedStream: Clinical Risk NLP \& Healthcare Analytics Dashboard

#### A complete end‑to‑end healthcare analytics and NLP system built with synthetic but highly realistic clinical data, ICD‑10–like conditions, encounter simulations, and a machine‑learning model that classifies patient risk from clinical notes.

#### The project integrates data engineering, NLP, machine learning, and interactive visualization into one cohesive, portfolio‑ready solution.

#### 

* #### **Live Dashboard**

#### &nbsp;       **https://medstream-dashboard.streamlit.app**

#### 

* #### **Introduction**

#### &nbsp;    Healthcare systems generate massive volumes of unstructured clinical                                              notes every day. These notes contain essential information about  patient condition, risk level, and care needs—but reviewing them manually is slow, inconsistent, and resource‑intensive.

#### 

#### &nbsp;     MedStream demonstrates how hospitals can use NLP and analytics to automatically interpret clinical notes, classify patient risk, and visualize trends in patient outcomes.

#### The project uses synthetic healthcare data that mimics real‑world patterns, making it safe, reproducible, and ideal for learning and portfolio demonstration.

#### 

* #### **Problem Statement**

#### Hospitals struggle with:

#### 

* #### Large volumes of unstructured clinical notes
* #### Difficulty identifying high‑risk patients early
* #### Limited visibility into patient outcomes and risk trends
* #### Manual review processes that are slow and inconsistent

#### 

#### There is a need for a system that can:

#### &nbsp;         Automatically classify clinical risk

#### &nbsp;         Provide real‑time analytics

#### &nbsp;         Support clinicians with actionable insights

#### &nbsp;         Operate safely using synthetic data

#### 

* #### **Project Objectives**

#### Generate realistic synthetic healthcare data (patients, encounters, clinical notes). Build an NLP model to classify clinical notes into high, medium, or low risk. Create an interactive Streamlit dashboard for analytics and real‑time predictions. Simulate ICD‑10–like conditions, encounter patterns, and severity‑based LOS. Provide a portfolio‑ready demonstration of healthcare analytics and NLP integration.

#### 

* #### Methodology

#### &nbsp;  **1. Synthetic Data Generation**

#### &nbsp;     A custom Python generator creates:

#### 

#### 400+ patients with age, gender, ICD‑10–like conditions, and comorbidities

#### 1000+ encounters with realistic patterns:

#### &nbsp;         ED → Inpatient → Outpatient

#### &nbsp;         LOS tied to severity

#### &nbsp;         Readmission probability tied to comorbidities

#### &nbsp;         50 clinical notes balanced across:

* #### high\_risk
* #### medium\_risk
* #### low\_risk

#### 

#### **2. NLP Pipeline**

#### &nbsp;      \* TF‑IDF vectorization (1–2 grams, 2000 features)

#### &nbsp;      \* Logistic Regression classifier

#### &nbsp;      \* Stratified train/test split

#### &nbsp;      \* Model saved as .pkl for dashboard use

#### 

#### 3\. **Dashboard Development**



#### &nbsp;      \* Built with Streamlit, the dashboard includes:

#### &nbsp;      \* Patient, encounter, and note metrics

#### &nbsp;      \* Risk distribution visualization

#### LOS by risk category

#### Real‑time clinical note risk prediction

#### Probability breakdown chart

#### 

* #### Technologies Used

#### &nbsp;   \* Python 3.10+

#### &nbsp;   \* Pandas – data manipulation

#### &nbsp;   \* NumPy – numerical operations

#### &nbsp;   \* Scikit‑learn – NLP + ML model

#### &nbsp;   \* Streamlit – interactive dashboard

#### &nbsp;   \* Plotly Express – visualizations

#### &nbsp;   \* Joblib – model persistence

#### &nbsp;   \* Synthetic data generation – custom Python logic

#### 

#### Models

#### NLP Model: 

* #### Logistic Regression

#### &nbsp;   Input: TF‑IDF vectorized clinical notes

#### &nbsp;   Output: Risk category (high, medium, low)

#### 

#### &nbsp;       => **Achieved 100% accuracy on synthetic test data due to**:

#### &nbsp;                         \* Balanced dataset

#### &nbsp;                         \* Distinct language patterns

#### &nbsp;                         \* Clean synthetic generation

#### Why Logistic Regression?

#### &nbsp;                      => Fast

#### 

#### **Interpretable**

#### &nbsp;             => Works extremely well with TF‑IDF text features

#### &nbsp;             => Ideal for structured synthetic datasets

#### 

#### **Analysis \& Interpretation**



#### **1. Risk Distribution**

#### &nbsp;     The dataset shows a balanced distribution across risk categories, 

#### &nbsp;     enabling fair model training.

#### 2\. **LOS by Risk**

#### &nbsp;     High‑risk patients show longer LOS due to severe conditions (CHF, COPD,

#### &nbsp;     CKD).

#### &nbsp;           => Medium‑risk patients show moderate LOS with borderline labs or

#### &nbsp;              chronic issues.

#### &nbsp;           => Low‑risk patients have minimal LOS or outpatient encounters.

#### 

#### 3\. **Model Behavior**

#### &nbsp;        The model correctly identifies:

#### &nbsp;           => High‑risk → acute deterioration, severe symptoms

#### &nbsp;           => Medium‑risk → chronic but concerning symptoms

#### &nbsp;           => Low‑risk → stable, routine follow‑ups

#### 

#### 4\. **Dashboard Insights**

#### Users can:

#### &nbsp;       Explore patient and encounter volumes

#### &nbsp;       Visualize risk trends

#### &nbsp;       Predict risk from new clinical notes

#### &nbsp;       Understand model confidence via probability charts

#### 

#### **Findings**

#### &nbsp;   Synthetic data can effectively simulate real‑world healthcare patterns.

#### &nbsp;   NLP models can classify risk accurately when trained on balanced, 

#### &nbsp;   well‑structured notes.

#### &nbsp;   Encounter patterns (ED → inpatient → follow‑up) create realistic LOS and

#### &nbsp;   readmission trends.

#### 

#### &nbsp;   Streamlit dashboards provide intuitive, real‑time clinical insights.

#### 

#### **Lessons Learned**

#### Balanced datasets dramatically improve NLP model performance.

#### 

#### Synthetic data generation requires careful design to mimic real clinical workflows.

#### 

#### TF‑IDF + Logistic Regression is a strong baseline for clinical text classification.

#### 

#### Dashboard usability improves when metrics, charts, and predictions are integrated seamlessly.

#### 

#### **Conclusion**

#### MedStream successfully demonstrates how healthcare organizations can use NLP and analytics to interpret clinical notes, classify patient risk, and visualize outcomes.

#### The project showcases a complete pipeline—from data generation to model deployment—using safe, synthetic data suitable for learning and portfolio presentation.

#### 

#### **Next Steps \& Improvements**

#### &nbsp;\* Add SHAP explainability for model predictions

#### &nbsp;\* Expand dataset to 200–500 clinical notes

#### &nbsp;\* Add filters (age, condition, encounter type) to the dashboard

#### &nbsp;\* Deploy the dashboard publicly via Streamlit Cloud or Railway

#### &nbsp;\* Add a FastAPI endpoint for model inference

#### &nbsp;\* Integrate time‑series analysis for patient trajectories

#### &nbsp;\* Add readmission prediction model as a second ML component

#### 

#### 

#### 

#### &nbsp;               ┌────────────────────┐

#### &nbsp;               │   Synthetic Patients    │

#### &nbsp;               └──────────┬─────────┘

#### &nbsp;                             │

#### &nbsp;               ┌──────────▼──────────┐

#### &nbsp;               │   Synthetic Encounters    │

#### &nbsp;               └──────────┬──────────┘

#### &nbsp;                             │

#### &nbsp;               ┌──────────▼──────────┐

#### &nbsp;               │  Clinical Notes (50)      │

#### &nbsp;               └──────────┬──────────┘

#### &nbsp;                             │

#### &nbsp;               ┌──────────▼──────────┐

#### &nbsp;               │   NLP Model (TF-IDF)      │

#### &nbsp;               └──────────┬──────────┘

#### &nbsp;                             │

#### &nbsp;               ┌──────────▼──────────┐

#### &nbsp;               │ Streamlit Dashboard       │

#### &nbsp;               └─────────────────────┘

#### ```mermaid

#### flowchart TD

#### &nbsp;   A\[Synthetic Patients] --> B\[Synthetic Encounters]

#### &nbsp;   B --> C\[Clinical Notes (50)]

#### &nbsp;   C --> D\[NLP Model (TF-IDF + Logistic Regression)]

#### &nbsp;   D --> E\[Streamlit Dashboard]

#### 

#### 

#### ---

#### 

#### \# \*\*GitHub Badge Set\*\*

#### 

#### 

#### ```md

#### <p align="center">

#### 

#### &nbsp; <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />

#### &nbsp; <img src="https://img.shields.io/badge/Streamlit-1.30+-brightgreen?logo=streamlit" />

#### &nbsp; <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn" />

#### &nbsp; <img src="https://img.shields.io/badge/License-MIT-yellow" />

#### &nbsp; <img src="https://img.shields.io/badge/Data-Synthetic-purple" />

#### 

#### </p>

#### 

#### 

#### 

