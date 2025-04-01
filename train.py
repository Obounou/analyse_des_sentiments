import mlflow
import mlflow.sklearn  # Pour enregistrer le modèle avec MLflow
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd

# Charger un dataset d'exemple (Iris)
data = load_iris()
X, y = data.data, data.target

# Diviser les données en train et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Faire des prédictions
y_pred = model.predict(X_test)

# Définir l'URI MLflow pour le stockage local
mlflow.set_tracking_uri("file:///home/runner/work/analyse_des_sentiments/mlruns")
mlflow.set_experiment("Analyse des Sentiments")

# Enregistrer les paramètres et métriques avec MLflow
with mlflow.start_run():
    mlflow.log_param("model", "RandomForest")
    mlflow.log_metric("accuracy", accuracy_score(y_test, y_pred))
    mlflow.log_metric("precision", precision_score(y_test, y_pred, average="macro"))
    mlflow.log_metric("recall", recall_score(y_test, y_pred, average="macro"))

    # Enregistrer le modèle
    mlflow.sklearn.log_model(model, "model")
