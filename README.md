# 📊 Analyse des Sentiments

## 📝 Description
Ce projet vise à analyser les sentiments des avis clients à l'aide du **NLP** et de **BERT**. Il met en place un pipeline comprenant plusieurs étapes : **extraction des données**, **prétraitement**, **tokenisation** et **inférence** pour obtenir des insights exploitables.

## 🚀 Pipeline du projet
1. **Extraction des données** : Chargement et validation des avis clients depuis un fichier CSV.
2. **Prétraitement des données** : Nettoyage du texte (suppression des caractères spéciaux, conversion en minuscules, suppression des stopwords).
3. **Tokenisation** : Transformation des avis en tokens exploitables par BERT.
4. **Inférence** : Prédiction du sentiment des avis en utilisant un modèle de classification binaire basé sur BERT.
5. **Validation et tests** : Mise en place de tests unitaires pour chaque module du pipeline.

## 📂 Structure du projet
```
analyse_des_sentiments/
│── src/
│   ├── data_extraction.py       # Extraction et validation des avis depuis dataset.csv
│   ├── data_processing.py       # Nettoyage, suppression des stopwords et tokenisation des avis
│   ├── inference.py             # Inférence et prédiction du sentiment des avis
│   ├── model.py                 # Chargement du modèle BERT pour la classification
│
│── tests/
│   ├── unit/
│   │   ├── test_data_extraction.py  # Tests unitaires de data_extraction.py
│   │   ├── test_data_processing.py  # Tests unitaires de data_processing.py
│   │   ├── test_inference.py        # Tests unitaires de inference.py
│   │   ├── test_model.py            # Tests unitaires du modèle
│
│── dataset.csv                # Données brutes d'entraînement et de test
│── dataset_tokenized.csv       # Données tokenisées et prétraitées
│── README.md                   # Documentation du projet
│── requirements.txt            # Dépendances Python requises
```

## ✅ Améliorations
- **Gestion des erreurs robuste** : Validation des données à chaque étape du pipeline.
- **Optimisation des performances** : Utilisation de `torch.no_grad()` pour accélérer l'inférence.
- **Meilleure modularité** : Chaque étape du pipeline est encapsulée dans des modules distincts.
- **Tests unitaires complets** : Garantir la fiabilité du pipeline avec des tests automatisés.


  # Partie 2 :

  # 📌 Analyse des Sentiments avec MLOps

## 📖 Description du Projet
Ce projet met en place un pipeline MLOps pour l'analyse des sentiments, incluant le prétraitement des données, l'entraînement du modèle, l'évaluation et le monitoring automatique via GitHub Actions.

## 🏗️ Architecture du Projet
Le projet est structuré comme suit :
```
.
├── .github/workflows/
│   ├── build.yml         # Build et installation des dépendances
│   ├── evaluate.yml      # Évaluation automatique et monitoring des performances
│   ├── release.yml       # Déploiement du modèle si la performance est satisfaisante
│   └── test.yml          # Tests unitaires et validation du pipeline
│
├── app.py                # API Flask pour faire des prédictions
├── train.py              # Script d'entraînement du modèle
├── evaluate.py           # Évaluation du modèle sur les données test
├── generate_evaluation_results.py  # Génère les résultats d'évaluation en JSON
├── generate_report.py     # Convertit les résultats en CSV pour analyse
├── monitor.py             # Vérifie la performance du modèle
│
├── requirements.txt       # Liste des dépendances Python
├── Dockerfile             # Conteneurisation de l'application
├── tests/unit/            # Dossier contenant les tests unitaires
├── README.md              # Documentation du projet
└── .gitignore             # Fichiers à exclure du dépôt
```

## 🚀 Installation et Exécution
### 1️⃣ Prérequis
- Python 3.9+
- Docker (optionnel)
- GitHub Actions configuré

### 2️⃣ Installation des dépendances
```bash
pip install -r requirements.txt
```

### 3️⃣ Entraînement du modèle
```bash
python train.py
```

### 4️⃣ Génération et évaluation des résultats
```bash
python generate_evaluation_results.py
python evaluate.py
python generate_report.py
```

### 5️⃣ Lancer l'API Flask
```bash
python app.py
```

## 🔬 Monitoring et Performance
- **Évaluation automatique** : `evaluate.yml` est exécuté après chaque entraînement.
- **Seuil de précision** : Si la précision est inférieure à `0.75`, une alerte est générée.
- **Rapport CSV** : `performance_report.csv` est créé pour analyser les résultats.

## 📊 Automatisation avec GitHub Actions
Les workflows sont définis dans `.github/workflows/`. Voici le pipeline automatisé :
1. **build.yml** → Installe les dépendances et valide le code
2. **test.yml** → Exécute les tests unitaires
3. **evaluate.yml** → Évalue le modèle et surveille ses performances
4. **release.yml** → Déploie le modèle si les performances sont bonnes

## 📌 Exécution sur GitHub Actions
Pour exécuter `evaluate.yml` automatiquement :
```yaml
on:
  workflow_run:
    workflows: ["Build"]
    types:
      - completed
```

## 💡 Améliorations possibles
- Ajouter une alerte Slack pour les performances critiques
- Enregistrer les métriques dans une base de données
- Améliorer la robustesse du modèle avec des données augmentées

---
🚀 **Projet développé avec une approche MLOps pour une gestion efficace du cycle de vie du modèle !**


