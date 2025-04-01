import pandas as pd
import json

# Charger les résultats de l’évaluation
with open("evaluation_results.json", "r") as f:
    results = json.load(f)

# Convertir en DataFrame
df = pd.DataFrame([results])

# Sauvegarder le rapport
df.to_csv("performance_report.csv", index=False)
print("Rapport de performance généré !")
