from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from joblib import load
import xgboost as xgb

# Charger le modèle
model_path = "../data/xgbclassifier.pkl"
model = load(model_path)

optimal_threshold = np.load('../data/optimal_threshold.npy').item()

data = pd.read_csv('../data/df_test.csv')

# Initialiser l'application Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue"

# Endpoint pour obtenir des prédictions en fonction de l'ID du client
@app.route('/predict/<int:client_id>', methods=['GET'])
def predict(client_id):
    # Rechercher les données du client avec cet ID
    client_data = data[data['SK_ID_CURR'] == client_id].drop(columns=['SK_ID_CURR'])

    if client_data.empty:
        return jsonify({'error': 'Client not found'}), 404

    # Faire la prédiction avec le modèle XGBoost
    proba = model.predict_proba(client_data).tolist()[0][1]
    prediction = 0 if proba < optimal_threshold else 1

    # Retourner la prédiction sous forme JSON
    return jsonify({
        'client_id': client_id,
        'proba': proba,
        'prediction': prediction
    })

# Lancer l'application
app.run(host = '127.0.0.1', port=7000, debug=True)