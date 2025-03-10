import sys
import os
import unittest
from typing import List

# Ajouter le dossier parent pour que Python reconnaisse "src"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Importer les fonctions depuis data_processing.py
from src.data_processing import normalize_text, remove_stopwords, tokenize_text, preprocess_text

class TestDataProcessing(unittest.TestCase):
    """ Teste les fonctions de traitement des avis. """

    def test_normalize_text(self):
        """ Vérifie si normalize_text supprime bien les accents et caractères spéciaux. """
        text = "C'est génial ! Éléphant & télé."
        expected = "c est genial elephant tele"
        self.assertEqual(normalize_text(text), expected)

    def test_remove_stopwords(self):
        """ Vérifie si remove_stopwords supprime bien les mots inutiles. """
        text = "this is a great product with many features"
        expected = "great product many features"  # Sans les stopwords
        self.assertEqual(remove_stopwords(text), expected)

    def test_tokenize_text(self):
        """ Vérifie si tokenize_text applique correctement le tokenizer BERT. """
        text = "Machine learning is amazing"
        tokens = tokenize_text(text)
        self.assertIsInstance(tokens, list)  # Vérifie que le résultat est une liste
        self.assertGreater(len(tokens), 0)   # Vérifie qu'il y a bien des tokens

    def test_preprocess_text(self):
        """ Vérifie si preprocess_text applique tout le pipeline correctement. """
        text = "C'est un excellent produit, vraiment utile !"
        tokens = preprocess_text(text)
        self.assertIsInstance(tokens, list)  # Vérifie que c'est une liste
        self.assertGreater(len(tokens), 0)   # Vérifie qu'il y a au moins un token

if __name__ == "__main__":
    unittest.main()
