import streamlit as st
import pandas as pd
import numpy as np
import joblib
from collections import Counter

# Load model and features
model = joblib.load("protein_model.pkl")
feature_cols = joblib.load("feature_columns.pkl")

# 20 standard amino acids
AMINO_ACIDS = list("ACDEFGHIKLMNPQRSTVWY")

# Function to compute AAC
def compute_aac(seq):
    seq = seq.upper()
    counts = Counter(seq)
    total = len(seq)
    return [counts.get(aa, 0)/total for aa in AMINO_ACIDS]

st.title("Protein Class Prediction App")

st.write("This app uses sequence-based and numeric features to predict the **functional class** of a protein.")

# Input fields
seq_input = st.text_area("Enter protein sequence (letters only):", height=200)

# Numeric properties (optional input)
massa = st.number_input("Molecular Mass", value=20000.0)
pI = st.number_input("Isoelectric Point", value=7.0)
hidrof = st.number_input("Hydrophobicity", value=0.15)
carga = st.number_input("Total Charge", value=5.0)
polar = st.number_input("Polar Proportion", value=0.2)
apolar = st.number_input("Apolar Proportion", value=0.4)

if st.button("Predict"):
    if len(seq_input) < 10:
        st.error("Sequence must have at least 10 amino acids.")
    else:
        seq_length = len(seq_input)

        # Compute AAC
        aac_values = compute_aac(seq_input)

        # Combine features
        input_data = [massa, pI, hidrof, carga, polar, apolar, seq_length] + aac_values
        input_df = pd.DataFrame([input_data], columns=feature_cols)

        # Prediction
        pred = model.predict(input_df)[0]
        probs = model.predict_proba(input_df)[0]

        st.subheader(f"Predicted Class: **{pred}**")
        st.write("Prediction Probabilities:")
        prob_df = pd.DataFrame([probs], columns=model.classes_)
        st.dataframe(prob_df.style.highlight_max(axis=1))
