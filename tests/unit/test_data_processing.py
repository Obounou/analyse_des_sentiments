import sys
import os
import unittest
import pandas as pd
from io import StringIO

# Ajouter le dossier parent au chemin pour que Python reconnaisse "src" comme un module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Importer les fonctions de traitement des données
from src.data_processing import clean_text, remove_stopwords, tokenize_text, process_reviews

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        """Préparation avant chaque test : création d'un DataFrame temporaire."""
        data = {
            "content": [
                "C'est un très bon produit ! 👍", 
                "Je déteste ce service...", 
                "Neutre.", 
                "", 
                "Le prix est trop élevé."
            ]
        }
        self.df = pd.DataFrame(data)

    def test_clean_text(self):
        """Vérifie si la fonction clean_text nettoie correctement le texte."""
        cleaned = clean_text("C'est Génial!!! 123 😊")
        self.assertEqual(cleaned, "cest genial")

    def test_remove_stopwords(self):
        """Vérifie si la suppression des stopwords fonctionne."""
        text = "this is a simple test with some stopwords"
        cleaned_text = remove_stopwords(text)
        self.assertNotIn("is", cleaned_text)
        self.assertNotIn("a", cleaned_text)
        self.assertNotIn("with", cleaned_text)

    def test_tokenize_text(self):
        """Vérifie si la tokenisation BERT fonctionne correctement."""
        tokens = tokenize_text("This is a test")
        self.assertIsInstance(tokens, list)
        self.assertGreater(len(tokens), 0)

    def test_process_reviews(self):
        """Vérifie si le pipeline de traitement des avis fonctionne."""
        processed_df = process_reviews(self.df)
        self.assertIn("cleaned_content", processed_df.columns)
        self.assertIn("tokenized_content", processed_df.columns)
        self.assertFalse(processed_df["cleaned_content"].isnull().values.any())
        self.assertFalse(processed_df["tokenized_content"].isnull().values.any())

if __name__ == "__main__":
    unittest.main()
