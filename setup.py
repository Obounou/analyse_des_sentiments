from setuptools import setup, find_packages

setup(
    name='analyse_des_sentiments',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',  # Liste des dépendances
        # Ajoute toutes les autres dépendances que ton projet utilise
    ],
)
