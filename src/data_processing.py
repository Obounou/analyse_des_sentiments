import sys
import os
import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from transformers import AutoTokenizer

# Ajouter "src" au chemin pour éviter l'erreur ModuleNotFoundError
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importer la fonction de chargement des données
from src.data_extraction import load_reviews_data

# Télécharger les stopwords si nécessaire
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Charger le tokenizer BERT
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


def clean_text(text):
    """ Nettoie le texte en supprimant les caractères spéciaux et les chiffres. """
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)  # Supprime caractères spéciaux et chiffres
        text = re.sub(r'\s+', ' ', text).strip()  # Supprime les espaces inutiles
        return text
    return ""


def remove_stopwords(text):
    """ Supprime les stopwords du texte. """
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


def tokenize_text(text):
    """ Tokenise un texte avec le tokenizer BERT. """
    return tokenizer.tokenize(text)


def process_reviews(df):
    """ Applique le nettoyage, suppression de stopwords et tokenisation sur un DataFrame. """
    if 'content' not in df.columns:
        raise ValueError("La colonne 'content' est absente du DataFrame.")
    
    df['cleaned_content'] = df['content'].apply(clean_text)
    df['cleaned_content'] = df['cleaned_content'].apply(remove_stopwords)
    df['tokenized_content'] = df['cleaned_content'].apply(tokenize_text)

    print("✅ Traitement des avis terminé.")
    return df


# ✅ Tester la fonction principale
if __name__ == "__main__":
    df = load_reviews_data()
    if df is not None:
        df = process_reviews(df)
        print(df[['content', 'cleaned_content', 'tokenized_content']].head())
