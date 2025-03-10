import sys
import os
import unittest
import pandas as pd

# Ajouter le dossier parent au chemin pour que Python reconnaisse "src" comme un module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Importer la fonction de chargement des données
from src.data_extraction import load_reviews_data

class TestDataExtraction(unittest.TestCase):

    def setUp(self):
        """
        Préparation avant chaque test : création d'un fichier CSV temporaire.
        """
        self.test_file = "test_dataset.csv"
        data = {
            "content": ["Avis positif", "Avis négatif", "Neutre", None, "Autre avis"],
            "score": [5, 1, 3, 2, None],
            "at": ["2024-01-01", "2023-12-15", "2023-11-30", None, "2024-02-10"]
        }
        df = pd.DataFrame(data)
        df.to_csv(self.test_file, index=False)

    def tearDown(self):
        """
        Suppression du fichier temporaire après les tests.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_valid_file(self):
        """
        Vérifie si le fichier est bien chargé et contient les bonnes colonnes.
        """
        df = load_reviews_data(self.test_file)
        self.assertIsNotNone(df)
        self.assertTrue("content" in df.columns)
        self.assertTrue("score" in df.columns)
        self.assertTrue("at" in df.columns)

    def test_missing_file(self):
        """
        Vérifie si une erreur est levée lorsqu'on essaie de charger un fichier inexistant.
        """
        df = load_reviews_data("fichier_inexistant.csv")
        self.assertIsNone(df)

    def test_missing_columns(self):
        """
        Vérifie si une erreur est levée lorsque des colonnes essentielles sont absentes.
        """
        invalid_data = {"text": ["Hello", "World"], "date": ["2023-01-01", "2023-02-01"]}
        df_invalid = pd.DataFrame(invalid_data)
        df_invalid.to_csv(self.test_file, index=False)

        df = load_reviews_data(self.test_file)
        self.assertIsNone(df)

    def test_cleaning_data(self):
        """
        Vérifie que les valeurs manquantes sont bien supprimées.
        """
        df = load_reviews_data(self.test_file)
        self.assertFalse(df["content"].isnull().values.any())
        self.assertFalse(df["at"].isnull().values.any())

if __name__ == "__main__":
    unittest.main()
