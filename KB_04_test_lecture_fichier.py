#Kawthar Bouguima Fichier test n°3 Lecture de fichiers csv
from KB_02_listes_type import *
from outils_csv import *


liste_fichiers = [
    "DONNEES/KB_data_00.csv",
    "DONNEES/KB_data_01.csv",
    "DONNEES/KB_data_05.csv",
    "DONNEES/KB_data_20.csv",
    "DONNEES/KB_data_100.csv"]


for i in range(0, len(liste_fichiers), 1):
    fichier = liste_fichiers[i]
    print(f"\n*** Début du traitement du fichier : {fichier} ***")
    entetes, donnees = lecture_fichier_csv(fichier, ";", "utf-8", 1)
    liste_tarif = liste_de_listes_trf(donnees)
    print(f"Le fichier {fichier} contient {len(liste_tarif)} lignes de données.")

    if (len(donnees)) < 18:
        print("Données lues :")
        affiche_liste_tarif(liste_tarif)
