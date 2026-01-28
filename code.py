"""
Parcours d'explorateurs - Analyse de graphe d'aventure.

Ce script charge et analyse un fichier CSV contenant les noeuds et arêtes d'un 
graphe d'aventure, en identifiant les points de départ, les liaisons entre noeuds 
et les points d'arrivée.
"""

import pandas as pd

# Charger le fichier CSV contenant les données de parcours
df = pd.read_csv("parcours_explorateurs_completed.csv")

# Extraire les arêtes de type "départ" (points de départ de l'aventure)
liste_depart = df[df["type_aretes"] == "depart"]

# Créer un dictionnaire qui associe chaque noeud amont à son noeud aval
# Cela représente les transitions possibles entre les noeuds du graphe
dict_parcours = dict(zip(df["noeud_amont"], df["noeud_aval"]))

# Extraire les points d'arrivée (noeuds finaux de type "arrivée")
# Utiliser un set pour éviter les doublons
set_arrivees = set(df[df["type_aretes"] == "arrivee"]["noeud_aval"])

if __name__ == "__main__":
    # Afficher les données chargées
    print(liste_depart)
    
    # Afficher les statistiques du graphe
    print(f"Nombre de départs : {len(liste_depart)}")
    print(f"Nombre de liaisons dans le dictionnaire : {len(dict_parcours)}")
    print(f"Nombre de points d'arrivée : {len(set_arrivees)}")

