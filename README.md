# Protein Classification – Bioinformatics + Machine Learning

This project demonstrates an **AI-driven pipeline for protein classification** using a combination of:
- **Sequence-based features (Amino Acid Composition)**
- **Physicochemical descriptors (molecular weight, isoelectric point, hydrophobicity, etc.)**

It mimics early stage **protein function prediction workflows** often seen in **biotherapeutic research and AI-driven protein engineering**.

---

## Dataset
- **Source:** [Bioinformatics Protein Dataset (Simulated)](https://www.kaggle.com/datasets/gallo33henrique/bioinformatics-protein-dataset-simulated)
- **Contents:**
  - ~20,000 protein sequences (train + test)
  - Columns include:
    - Protein sequence
    - Mass, isoelectric point, hydrophobicity
    - Polar/apolar composition
    - Protein class labels: *Estrutural, Receptora, Enzima, Transporte, Outras*

---

## Key Achievements

### 1. **Data Exploration and Insights**
- **Sequence Length Distribution**  
  Most proteins are between **100–300 amino acids**, with a nearly uniform distribution.  
  This aligns with typical ranges for structured proteins.
  
  <img width="548" height="313" alt="Sequence Length Distribution" src="https://github.com/user-attachments/assets/46ef5052-81f2-49ad-acce-0d13758899e8" />


- **Correlation Analysis**  
  - **Isoelectric point (pI)** correlates strongly with **total charge**.
  - **Hydrophobicity** correlates with **apolar proportion** – biologically intuitive.

- **Class Distribution**  
  Classes are **balanced** (~3200 samples each), which ensures unbiased modeling.

---

### 2. **Feature Engineering**
- **Added `seq_length`** as a numeric feature.
- **Extracted Amino Acid Composition (AAC):**  
  For each sequence, computed the proportion of 20 amino acids → 20 biologically relevant features.
- Combined **7 physicochemical descriptors** with **20 AAC features** (27 features total).

---

### 3. **Modeling Results**

#### **Model 1: Physicochemical Descriptors Only**
- **Algorithm:** Random Forest Classifier
- **Accuracy:** ~20%
- **Insights:**
  - Numeric properties alone **are insufficient** for protein class prediction.
  - Important features: **Isoelectric Point, Polar/Apolar ratios, Hydrophobicity**.

#### **Model 2: Descriptors + AAC Features**
- **Algorithm:** Random Forest Classifier
- **Accuracy:** ~20.4% (slightly improved)
- **Feature Importance:**
  - **AAC_L (Leucine)**, **AAC_C (Cysteine)**, and other AAC features dominate the top features.
  - Shows **sequence content is critical** for prediction.

> **Why accuracy is low:**  
> This dataset is **simulated with high complexity and no evolutionary/3D structure data**, so it lacks strong sequence-function patterns.  
> In real-world scenarios, adding **evolutionary features (PSSM, embeddings)** dramatically improves accuracy.

---

### 4. **Interactive Streamlit Dashboard**

The `app.py` dashboard:
- Accepts a **protein sequence** (and optional numeric descriptors).
- Computes AAC features.
- **Predicts protein class** using the trained model.
- Displays **class probabilities** for interpretability.

  <img width="688" height="746" alt="Interactive Streamlit Dashboar" src="https://github.com/user-attachments/assets/67ad8907-d1b1-45eb-a286-f638b90e4896" />


Run locally:
```bash
pip install -r requirements.txt
streamlit run app.py
