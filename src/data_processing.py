import sys
import os
import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from transformers import AutoTokenizer

# Ajouter le dossier parent au chemin pour que Python reconnaisse "src" comme module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importer la fonction de chargement des données
from src.data_extraction import load_reviews_data

# Télécharger les stopwords si nécessaire
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Charger le tokenizer BERT
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


def clean_text(text):
    """
    Nettoie le texte en supprimant les caractères spéciaux, les nombres et les espaces inutiles.
    
    :param text: Texte brut.
    :return: Texte nettoyé.
    """
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)  # Supprime les caractères spéciaux et nombres
        text = re.sub(r'\s+', ' ', text).strip()  # Supprime les espaces inutiles
        return text
    return ""


def remove_stopwords(text):
    """
    Supprime les stopwords du texte.
    
    :param text: Texte nettoyé.
    :return: Texte sans stopwords.
    """
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


def tokenize_text(text):
    """
    Tokenise un texte avec le tokenizer BERT.
    
    :param text: Texte nettoyé.
    :return: Liste de tokens.
    """
    return tokenizer.encode(text, add_special_tokens=True)


def process_reviews(df):
    """
    Applique les étapes de nettoyage et de tokenisation sur le DataFrame.
    
    :param df: DataFrame contenant les avis.
    :return: DataFrame transformé.
    """
    if 'content' not in df.columns:
        raise ValueError("La colonne 'content' est absente du DataFrame.")
    
    df['cleaned_content'] = df['content'].apply(clean_text)
    df['cleaned_content'] = df['cleaned_content'].apply(remove_stopwords)
    df['tokenized_content'] = df['cleaned_content'].apply(tokenize_text)

    print("Traitement des avis terminé.")
    return df


# Tester la fonction
if __name__ == "__main__":
    df = load_reviews_data()
    if df is not None:
        df = process_reviews(df)
        print(df[['content', 'cleaned_content', 'tokenized_content']].head())