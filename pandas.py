import pandas as pd

# Charger le fichier Excel
df = pd.read_excel('doublons.xlsx')

# Renommer les colonnes pour plus de clarté
df.columns = ['Colonne1', 'Colonne2']

# Obtenir les valeurs uniques de chaque colonne
valeurs_uniques_col1 = df['Colonne1'].unique()
valeurs_uniques_col2 = df['Colonne2'].unique()

# Afficher les résultats
print("Valeurs uniques de la Colonne 1 :", valeurs_uniques_col1)
print("Valeurs uniques de la Colonne 2 :", valeurs_uniques_col2)
