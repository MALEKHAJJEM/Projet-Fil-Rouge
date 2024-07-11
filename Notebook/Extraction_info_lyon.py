import pandas as pd
import os
import glob

# Définir le répertoire contenant les fichiers CSV
directory_path = r'C:\Users\Administrateur\csv-2018-2019-2020'  # Remplacez par le chemin de votre répertoire

# Créer un répertoire pour les fichiers filtrés (si nécessaire)
filtered_directory_path = os.path.join(directory_path, 'filtered')
os.makedirs(filtered_directory_path, exist_ok=True)

# Définir la colonne et la valeur à filtrer
column_name = 'Organisme'
value_to_filter = 'ATMO AUVERGNE-RHÔNE-ALPES'

# Fonction pour normaliser les noms de colonnes
def normalize_column_names(df):
    df.columns = df.columns.str.strip().str.lower()
    return df

# Normaliser le nom de la colonne à filtrer
normalized_column_name = column_name.strip().lower()

# Parcourir tous les fichiers CSV dans le répertoire
for csv_file in glob.glob(os.path.join(directory_path, '*.csv')):
    try:
        # Charger le fichier CSV
        df = pd.read_csv(csv_file,delimiter=';',encoding='latin-1')
        
        # Normaliser les noms de colonnes
        df = normalize_column_names(df)
        
        # Afficher les noms de colonnes pour vérification
        #print(f'Noms des colonnes dans {csv_file} : {df.columns.tolist()}')
        
        # Vérifier si la colonne existe dans le dataframe
        if normalized_column_name in df.columns:
            # Filtrer les lignes où la colonne normalisée a la valeur normalisée
            filtered_df = df[df[normalized_column_name] == value_to_filter]
            
            # Déterminer le nom du fichier de sortie
            base_name = os.path.basename(csv_file)
            filtered_file_path = os.path.join(filtered_directory_path, f'filtered_{base_name}')
            
            # Sauvegarder les lignes filtrées dans un nouveau fichier CSV
            filtered_df.to_csv(filtered_file_path, index=False)
            
            print(f'Fichier filtré sauvegardé : {filtered_file_path}')
        else:
            print(f'Erreur : La colonne "{column_name}" (normalisée en "{normalized_column_name}") n\'existe pas dans le fichier {csv_file}')
    except pd.errors.EmptyDataError:
        print(f'Erreur : Le fichier {csv_file} est vide.')
    except pd.errors.ParserError:
        print(f'Erreur : Il y a une erreur de syntaxe dans le fichier {csv_file}.')
    except Exception as e:
        print(f'Erreur inattendue avec le fichier {csv_file}: {e}')