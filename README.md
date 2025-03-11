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


