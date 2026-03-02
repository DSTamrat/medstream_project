import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import os

BASE = r"C:\Users\PC\OneDrive\Desktop\medstream_project"

notes = pd.read_csv(os.path.join(BASE, "data", "clinical_notes.csv"))

X = notes["note_text"]
y = notes["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2), max_features=2000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

clf = LogisticRegression(max_iter=2000)
clf.fit(X_train_vec, y_train)

print(classification_report(y_test, clf.predict(X_test_vec)))

joblib.dump(clf, os.path.join(BASE, "models", "note_classifier.pkl"))
joblib.dump(vectorizer, os.path.join(BASE, "models", "vectorizer.pkl"))

print("Model and vectorizer saved.")
