import sys
import os
import re
import unicodedata
import pandas as pd
from typing import List, Set

# Ajouter le dossier parent au chemin pour que Python reconnaisse "src" comme un module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importer la fonction pour charger les données
from src.data_extraction import load_reviews_data  

# Initialisation du tokenizer BERT
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Liste de stopwords (mots vides)
try:
    from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
    STOPWORDS: Set[str] = set(ENGLISH_STOP_WORDS)
except ImportError:
    STOPWORDS: Set[str] = {"and", "or", "the", "a", "an", "is", "it",
                           "this", "that", "to", "of", "in", "for", "on",
                           "le", "la", "et", "ou", "un", "une", "de", "du"}


def normalize_text(text: str) -> str:
    """
    Nettoie le texte : suppression des accents, conversion en minuscules,
    suppression des caractères spéciaux et des espaces inutiles.
    """
    if isinstance(text, str):
        # Supprimer les accents
        text_nfd = unicodedata.normalize('NFD', text)
        text_without_accents = "".join(ch for ch in text_nfd if unicodedata.category(ch) != 'Mn')

        # Convertir en minuscules
        text_lower = text_without_accents.lower()

        # Supprimer les caractères spéciaux et chiffres
        text_clean = re.sub(r'[^a-z\s]', '', text_lower)

        # Supprimer les espaces inutiles
        text_clean = re.sub(r'\s+', ' ', text_clean).strip()

        return text_clean
    return ""


def remove_stopwords(text: str, stopwords: Set[str] = STOPWORDS) -> str:
    """ Supprime les stopwords du texte. """
    words = text.split()
    meaningful_words = [word for word in words if word not in stopwords]
    return " ".join(meaningful_words)


def tokenize_text(text: str) -> List[str]:
    """ Tokenise un texte avec le tokenizer BERT. """
    return tokenizer.tokenize(text)


def preprocess_text(text: str) -> List[str]:
    """
    Applique le pipeline de traitement : nettoyage, suppression des stopwords et tokenisation.
    """
    clean = normalize_text(text)
    without_stopwords = remove_stopwords(clean)
    tokens = tokenize_text(without_stopwords)
    return tokens


if __name__ == "__main__":
    # Charger les données avec la fonction existante
    df = load_reviews_data()

    if df is not None and 'content' in df.columns:
        print("✅ Chargement réussi. Début du traitement des avis...")

        # Appliquer le prétraitement sur la colonne "content"
        df['tokenized_content'] = df['content'].apply(preprocess_text)

        # Afficher un aperçu des données transformées
        print(df[['content', 'tokenized_content']].head())

        # Sauvegarde des résultats
        output_path = "dataset_tokenized.csv"
        df.to_csv(output_path, index=False)
        print(f"✅ Traitement terminé. Fichier sauvegardé sous : {output_path}")
    else:
        print("❌ Erreur : Impossible de traiter les données (fichier manquant ou colonne absente).")
