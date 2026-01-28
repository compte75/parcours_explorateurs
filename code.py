"""
Parcours d'explorateurs - Analyse de graphe d'aventure.

Ce script charge et analyse un fichier CSV contenant les noeuds et arêtes d'un 
graphe d'aventure, en identifiant les points de départ, les liaisons entre noeuds 
et les points d'arrivée.
"""

import pandas as pd

if __name__ == "__main__":
# Charger le fichier CSV contenant les données de parcours
    edges_df = pd.read_csv("./parcours_explorateurs_completed.csv")
    strating_nodes =  edges_df[edges_df["type_aretes"] == "depart"]["noeud_amont"].tolist()





