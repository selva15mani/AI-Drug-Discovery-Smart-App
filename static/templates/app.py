from flask import Flask, render_template, request, jsonify
import joblib
from rdkit import Chem
from rdkit.Chem import Descriptors

app = Flask(_name_)

# Load trained AI model
model = joblib.load("drug_model.pkl")

# Function to predict drug properties
def predict_drug_properties(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        mw = Descriptors.MolWt(mol)  # Molecular Weight
        logp = Descriptors.MolLogP(mol)  # LogP
        prediction = model.predict([[mw, logp]])[0]  # AI Prediction
        return {"Molecular Weight": mw, "LogP": logp, "Effectiveness": prediction}
    except:
        return {"error": "Invalid SMILES notation"}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    smiles = data["smiles"]
    result = predict_drug_properties(smiles)
    return jsonify(result)

if _name_ == "_main_":
    app.run(debug=True)