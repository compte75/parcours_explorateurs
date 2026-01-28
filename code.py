"""
Parcours d'explorateurs 

Ce script charge et analyse un fichier CSV contenant les noeuds et arêtes d'un 
graphe d'aventure, en identifiant les points de départ, les liaisons entre noeuds 
et les points d'arrivée.


Variables:
ending_nodes = noeud_aval
edges = aretes
starting_nodes = noeud_amont
dict_upstream_downstream = dictionnaire des noeuds amont et aval
current_path = chemin courant
current_node = noeud courant
next_node = noeud suivant
build_explorateurs_paths = construire_les_chemins_des_explorateurs
edges_df = dataframe_des_aretes

"""
import pandas as pd

def prepare_data(edges_df):
    starting_nodes = edges_df[edges_df["type_aretes"] == "depart"]["noeud_amont"].tolist()
    dict_upstream_downstream = {row["noeud_amont"]: row["noeud_aval"] for _, row in edges_df.iterrows()}
    ending_nodes = set(edges_df[edges_df["type_aretes"] == "arrivee"]["noeud_aval"])
    return starting_nodes, dict_upstream_downstream, ending_nodes

    

def build_explorateurs_paths (starting_nodes, dict_upstream_downstream,ending_nodes):
    for starting_node in starting_nodes: 
        current_path = [starting_node]

        while current_path[-1] not in ending_nodes:
            current_node = current_path[-1]
            next_node = dict_upstream_downstream[current_node]
            current_path.append(next_node)

        
if __name__ == "__main__":

    edges_df = pd.read_csv("./parcours_explorateurs_completed.csv")
  
    starting_nodes, dict_upstream_downstream, ending_nodes = prepare_data(edges_df)
    explorateurs_paths = build_explorateurs_paths(starting_nodes, dict_upstream_downstream, ending_nodes)

    for explorateur_id, explorateur_path





