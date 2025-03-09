import pandas as pd
import os

# Définir le chemin du fichier
DATASET_PATH = "dataset.csv"

def load_reviews_data(filepath=DATASET_PATH):
    """
    Charge le fichier CSV contenant les avis et effectue des vérifications.
    
    :param filepath: Chemin du fichier CSV.
    :return: DataFrame contenant les avis nettoyés ou None si erreur.
    """
    try:
        # Vérifier si le fichier existe
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Erreur : Le fichier '{filepath}' n'existe pas.")

        # Charger le fichier CSV
        df = pd.read_csv(filepath, encoding='utf-8', low_memory=False)
        
        # Vérifier la présence des colonnes essentielles
        required_columns = {'content', 'score', 'at'}
        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(f"Colonnes manquantes dans le fichier : {missing_columns}")

        # Nettoyage des données
        df = df.dropna(subset=['content'])  # Supprimer les avis vides
        df['at'] = pd.to_datetime(df['at'], errors='coerce')  # Conversion de la date
        df = df.dropna(subset=['at'])  # Supprimer les dates invalides

        print("Données chargées avec succès.")
        return df

    except Exception as e:
        print(f"Erreur : {e}")
        return None

# Tester la fonction
if __name__ == "__main__":
    df = load_reviews_data()
    if df is not None:
        print(df.head())  # Afficher un aperçu des données
