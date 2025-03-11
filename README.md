# 📊 Analyse des Sentiments

## 📝 Description
Ce projet permet d'analyser les sentiments des avis clients à l'aide du **NLP** et de **BERT** pour la tokenisation. Il applique un pipeline de **prétraitement**, de **tokenisation** et de **clustering** pour obtenir des insights utiles.

## 📂 Structure du projet
analyse_des_sentiments/ │── src/ │ ├── data_extraction.py # Extraction des avis depuis dataset.csv │ ├── data_processing.py # Nettoyage et tokenisation des avis │ ├── inference.py # Inférence du modèle d'analyse │ ├── model.py # Modèle de classification des sentiments │── tests/ │ ├── unit/ │ │ ├── test_data_extraction.py # Tests unitaires de data_extraction.py │ │ ├── test_data_processing.py # Tests unitaires de data_processing.py │ │ ├── test_inference.py # Tests unitaires de inference.py │ │ ├── test_model.py # Tests unitaires du modèle │── dataset.csv # Données d'entraînement et de test │── dataset_tokenized.csv # Données après prétraitement │── README.md # Documentation du projet │── requirements.txt # Dépendances Python nécessaires