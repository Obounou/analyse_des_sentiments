from flask import Flask, request, jsonify
from transformers import pipeline

# Initialiser l'application Flask
app = Flask(__name__)

# Charger le modèle de prédiction de sentiment
classifier = pipeline("sentiment-analysis")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Récupérer le texte à partir de la requête
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Prédiction de sentiment
    result = classifier(text)

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Exposer l'API sur le port 5000
