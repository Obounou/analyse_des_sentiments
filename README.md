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

# Analyse des Sentiments avec MLOps

## 📌 Description du Projet
Ce projet utilise des modèles d'apprentissage automatique pour analyser les sentiments exprimés dans un ensemble de données textuelles. Il suit un pipeline MLOps bien défini et automatisé grâce à GitHub Actions.

---

## 🚀 Statut des Workflows GitHub Actions

![Build](https://github.com/votre-repo/analyse_des_sentiments/actions/workflows/build.yml/badge.svg)
![Test](https://github.com/votre-repo/analyse_des_sentiments/actions/workflows/test.yml/badge.svg)
![Évaluation](https://github.com/votre-repo/analyse_des_sentiments/actions/workflows/evaluate.yml/badge.svg)
![Release](https://github.com/votre-repo/analyse_des_sentiments/actions/workflows/release.yml/badge.svg)

Ces workflows automatisent le développement, la validation et le déploiement du modèle de machine learning.

---

## 🛠️ Pipeline MLOps
Le pipeline MLOps suit les étapes suivantes :

1. **Build** (`build.yml`)
   - Installe les dépendances
   - Vérifie la structure du projet
   - Prépare l'environnement

2. **Test** (`test.yml`)
   - Exécute les tests unitaires
   - Vérifie la robustesse et la performance du modèle

3. **Évaluation** (`evaluate.yml`)
   - Exécute le modèle sur des données de validation
   - Génère des métriques de performance

4. **Release** (`release.yml`)
   - Création et publication d'une nouvelle version du modèle
   - Génération de la documentation
   
---

## 🐳 Exécution avec Docker

Pour exécuter ce projet avec Docker :

1. **Cloner le dépôt**
   ```sh
   git clone https://github.com/votre-repo/analyse_des_sentiments.git
   cd analyse_des_sentiments
   ```

2. **Construire l'image Docker**
   ```sh
   docker build -t analyse_sentiments .
   ```

3. **Lancer le conteneur**
   ```sh
   docker run -p 8000:8000 analyse_sentiments
   ```

Cela démarre une API pour analyser des textes en temps réel.

---

## 📝 Contribuer
Les contributions sont les bienvenues !
1. Forkez le projet
2. Créez une branche (`git checkout -b feature-nouvelle-fonctionnalité`)
3. Committez vos modifications (`git commit -m "Ajout d'une nouvelle fonctionnalité"`)
4. Poussez votre branche (`git push origin feature-nouvelle-fonctionnalité`)
5. Ouvrez une Pull Request


---

## 📞 Contact
Pour toute question, ouvrez une issue ou contactez-nous par email à `mintsamalone@gmail.com`. 🚀

