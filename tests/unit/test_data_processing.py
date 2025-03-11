import sys
import os
import unittest
import pandas as pd

# ✅ Ajouter "src" au chemin pour éviter l'erreur ModuleNotFoundError
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

# ✅ Importer correctement les fonctions depuis src/data_processing.py
from data_processing import clean_text, remove_stopwords, tokenize_text, process_reviews

class TestDataProcessing(unittest.TestCase):
    """ Teste les fonctions de traitement des avis. """

    def test_clean_text(self):
        """ Vérifie que clean_text supprime bien les caractères spéciaux et met en minuscules. """
        text = "C'est génial ! Éléphant & télé. 123"
        expected = "cest genial elephant tele"
        self.assertEqual(clean_text(text), expected)

    def test_remove_stopwords(self):
        """ Vérifie que remove_stopwords supprime bien les stopwords. """
        text = "this is a great product with many features"
        expected = "great product many features"  # Suppression des stopwords
        self.assertEqual(remove_stopwords(text), expected)

    def test_tokenize_text(self):
        """ Vérifie que tokenize_text applique correctement le tokenizer BERT. """
        text = "Machine learning is amazing"
        tokens = tokenize_text(text)
        self.assertIsInstance(tokens, list)  # Vérifie que le résultat est une liste
        self.assertGreater(len(tokens), 0)   # Vérifie qu'il y a bien des tokens

    def test_process_reviews(self):
        """ Vérifie que process_reviews applique tout le pipeline sur un DataFrame. """
        data = {
            'content': [
                "This is an amazing product!",
                "Worst experience ever. Don't buy it.",
                "Simple, efficient, and useful."
            ]
        }
        df = pd.DataFrame(data)

        # Appliquer le traitement
        processed_df = process_reviews(df)

        # Vérifier que les colonnes sont créées
        self.assertIn('cleaned_content', processed_df.columns)
        self.assertIn('tokenized_content', processed_df.columns)

        # Vérifier que les valeurs sont correctes
        self.assertGreater(len(processed_df['cleaned_content'][0]), 0)
        self.assertGreater(len(processed_df['tokenized_content'][0]), 0)

if __name__ == "__main__":
    unittest.main()

