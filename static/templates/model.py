import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample drug dataset (Molecular Weight, LogP, Effectiveness)
data = [
    ("CCO", 46.07, -0.24, 1),
    ("CC(=O)O", 60.05, -0.64, 0),
    ("CCN", 45.08, -0.34, 1),
    ("CCOCC", 74.12, 0.12, 1),
    ("CCC(=O)O", 88.11, -0.23, 0)
]

df = pd.DataFrame(data, columns=["SMILES", "MolWt", "LogP", "Effectiveness"])

X = df[["MolWt", "LogP"]]
y = df["Effectiveness"]

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "drug_model.pkl")
print("✅ Model trained and saved as 'drug_model.pkl'")