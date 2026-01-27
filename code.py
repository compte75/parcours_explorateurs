# liste des noeuds de debut d'aventure 
# un dictionnaire qui associe à tout noeud amont son noeud aval
# set des neouds de fin d'aventure
 
import pandas as pd

df = pd.read_csv("parcours_explorateurs_completed.csv")
liste_depart = df[df["type_aretes"] == "depart"]


dict_parcours = dict((df["noeud_amont"], df["noeud_aval"]))


set_arrivees = set(df[df["type_aretes"] == "arrivee"]["noeud_aval"])


print (df_depart)
print(f"Nombre de départs : {len(liste_departs)}")
print(f"Nombre de liaisons dans le dictionnaire : {len(dict_parcours)}")
print(f"Nombre de points d'arrivée : {len(set_arrivees)}")

