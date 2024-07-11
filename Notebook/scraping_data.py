import requests
from bs4 import BeautifulSoup
import os

# URL de la page web contenant les fichiers CSV
url = 'https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/old/2020/'

# Répertoire de destination pour les fichiers CSV téléchargés
destination_folder = 'xml2020_files'
os.makedirs(destination_folder, exist_ok=True)

# Effectuer la requête GET pour obtenir le contenu de la page
response = requests.get(url)

# Vérifier que la requête a réussi
if response.status_code == 200:
    # Parser le contenu HTML de la page avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Trouver tous les liens vers les fichiers CSV
    links = soup.find_all('a')

    # Filtrer les liens pour obtenir uniquement ceux qui pointent vers des fichiers CSV
    xml_links = [link['href'] for link in links if link['href'].endswith('.xml')]

    # Télécharger chaque fichier CSV
    for xml_link in xml_links:
        xml_url = url + xml_link  # Construire l'URL complète du fichier CSV
        xml_filename = os.path.join(destination_folder, xml_link)

        # Effectuer la requête GET pour télécharger le fichier CSV
        xml_response = requests.get(xml_url)

        # Sauvegarder le fichier xml localement
        with open(xml_filename, 'wb') as file:
            file.write(xml_response.content)
        
        print(f"Fichier {xml_link} téléchargé et sauvegardé sous {xml_filename}")
else:
    print("Erreur lors de la requête vers le site web.")