import os
import subprocess

# Exemple de génération d'une version
def create_version():
    version = "0.1.0"  # Ici tu pourrais automatiser l'incrémentation de la version
    with open("VERSION.txt", "w") as version_file:
        version_file.write(version)
    print(f"Version {version} créée.")

# Exemple de création d'une archive (zip) pour la version
def create_archive():
    version = "0.1.0"
    subprocess.run(["tar", "-czf", f"release-{version}.tar.gz", "."])  # Crée un tar.gz du projet
    print(f"Archive {version} créée.")

if __name__ == "__main__":
    create_version()
    create_archive()
