import json

# Exemple de résultats d'évaluation du modèle
evaluation_results = {
    'accuracy': 0.85,
    'precision': 0.80,
    'recall': 0.75,
    'f1_score': 0.77
}

# Chemin vers le fichier JSON
file_path = 'evaluation_results.json'

# Sauvegarder les résultats dans un fichier JSON
with open(file_path, 'w') as f:
    json.dump(evaluation_results, f, indent=4)

print(f"Le fichier {file_path} a été généré avec succès.")
