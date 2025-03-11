import sys
import os
import re
import unicodedata
import pandas as pd
import nltk
from nltk.corpus import stopwords
from transformers import AutoTokenizer
from typing import List, Set

# ✅ Ajouter "src" au chemin pour éviter les erreurs d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ✅ Importer la fonction de chargement des données
from src.data_extraction import load_reviews_data

# ✅ Télécharger les stopwords si nécessaire
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# ✅ Charger le tokenizer BERT
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


def normalize_text(text: str) -> str:
    """ Nettoie le texte : suppression des accents, conversion en minuscules, suppression des caractères spéciaux et espaces inutiles. """
    if isinstance(text, str):
        text = unicodedata.normalize('NFD', text)  # Supprimer les accents
        text = "".join(ch for ch in text if unicodedata.category(ch) != 'Mn')
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)  # Supprime caractères spéciaux et chiffres
        text = re.sub(r'\s+', ' ', text).strip()  # Supprime espaces inutiles
        return text
    return ""


def remove_stopwords(text: str) -> str:
    """ Supprime les stopwords du texte. """
    words = text.split()
    meaningful_words = [word for word in words if word not in stop_words]
    return " ".join(meaningful_words)


def tokenize_text(text: str) -> List[str]:
    """ Tokenise un texte avec le tokenizer BERT. """
    return tokenizer.tokenize(text)


def preprocess_text(text: str) -> List[str]:
    """ Applique le pipeline de traitement : nettoyage, suppression des stopwords et tokenisation. """
    clean = normalize_text(text)
    without_stopwords = remove_stopwords(clean)
    tokens = tokenize_text(without_stopwords)
    return tokens


def process_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """ Applique le prétraitement sur un DataFrame contenant les avis. """
    if 'content' not in df.columns:
        raise ValueError("La colonne 'content' est absente du DataFrame.")
    
    df['cleaned_content'] = df['content'].apply(normalize_text)
    df['cleaned_content'] = df['cleaned_content'].apply(remove_stopwords)
    df['tokenized_content'] = df['cleaned_content'].apply(tokenize_text)

    print("✅ Traitement des avis terminé.")
    return df


# ✅ Tester la fonction principale
if __name__ == "__main__":
    df = load_reviews_data()

    if df is not None and 'content' in df.columns:
        print("✅ Chargement réussi. Début du traitement des avis...")
        df = process_reviews(df)

        # Afficher un aperçu des données transformées
        print(df[['content', 'cleaned_content', 'tokenized_content']].head())

        # Sauvegarde des résultats
        output_path = "dataset_tokenized.csv"
        df.to_csv(output_path, index=False)
        print(f"✅ Traitement terminé. Fichier sauvegardé sous : {output_path}")
    else:
        print("❌ Erreur : Impossible de traiter les données (fichier manquant ou colonne absente).")
