#Kawthar Bouguima TP projet partie 1 du 01/04/2025
#Modification le 19/04/2025 ajout de tri, fonction de lecture qui utilise listedeliste, et liste vide
#Modification le 24/04/2025 ajout de recherche d'occurences
"""
Ce fichier contient un menu conçu pour un utilisateur externe
"""

from KB_02_listes_type import *
from outils_csv import *


def afficher_menu():
    """
    Rôle : Affiche le menu principal de l'utilisateur.
    """
    print("*** MENU UTILISATEUR ***")
    print("1 - Ouvrir un fichier")
    print("2 - Filtrer les données")
    print("3 - Afficher les indicateurs statistiques")
    print("4 - Compter les occurences d'une valeur")
    print("5 - Quitter")



def analyseur():
    """
    Rôle : Gère l'interaction avec un utilisateur en proposant différentes tels que options :
        - Ouvrir un fichier CSV contenant des données sur les tarifs de train,
        - Filtrer les données chargées selon une gare (origine ou destination),
        - Afficher des indicateurs statistiques (minimum, maximum, moyenne, écart-type, mediane, modalités), trie si n'est pas triée
        - Recherche les occurrences d'une valeur
        - Quitter le programme.
    Préconditions :
    - Les fichiers CSV doivent exister aux emplacements indiqués dans la liste_fichiers.
    """
    liste_courante = []
    terminer = False
    liste_fichiers = [
    "DONNEES/KB_data_Final.csv",
    "DONNEES/KB_data_00.csv",
    "DONNEES/KB_data_05.csv",
    "DONNEES/KB_data_20.csv",
    "DONNEES/KB_data_100.csv"]
    while not terminer:
        afficher_menu()
        choix = input("Votre choix : ")
        
        if choix == "1":
            print("\n¤ Fichiers disponibles :")
            i = 0
            while i < len(liste_fichiers):
                print(f"{i + 1} - {liste_fichiers[i]}")
                i += 1
                
            #Test de bonne saisie du numéro de fichier
            valide = False
            while not valide:
                saisie = input("Entrez le numéro du fichier CSV : ")
                num_fichier = int(saisie)
                for k in range(1, len(liste_fichiers) + 1):
                    if num_fichier == k:
                        valide = True
                if not valide:
                    print("Numéro non valide. Réessayez.")
    
            nom_fichier = liste_fichiers[num_fichier -1]
            entete, donnees = lecture_fichier_csv(nom_fichier, ";", "utf-8", 1)
            liste_courante = liste_de_listes_trf(donnees)
            print(f"Ouverture du fichier {nom_fichier}")
            
            if len(donnees) < 21:
                print("Données lues :")
                affiche_liste_tarif(liste_courante)

        elif choix == "2":
            if len(liste_courante)== 0 :
                print("Aucune donnée chargée !")
            else:
                gare = input("Entrez la gare pour filtrer : ")
                type_filtre = input("Filtrer par origine (o) ou destination (d) ? ")
                if type_filtre == "o":
                    type_filtre = "origine"
                else:
                    type_filtre = "destination"

    
                liste_temp = filtrage(liste_courante, gare, type_filtre)
                if len(liste_temp) > 0:
                    liste_courante = liste_temp
                    print(f"{len(liste_courante)} enregistrements après filtrage.")
                    affiche_liste_tarif(liste_courante)
                else:
                    print("0 enregistrement après filtrage.")
                
        elif choix == "3":
            if len(liste_courante)==0:
                print("Aucune donnée disponible pour les statistiques.")
            else:
                #Seulement quand la liste est non vide
                min_val = tarif_minimum(liste_courante)
                max_val = tarif_maximum(liste_courante)
                moy = tarif_moyenne(liste_courante)
                et = ecart_type(liste_courante)
                print(f"- Nombre d'enregistrements : {len(liste_courante)}")
                print(f"- Prix Minimum : {min_val}")
                print(f"- Prix Maximum : {max_val}")
                print(f"- Prix Moyen : {moy}")
                print(f"- Écart-Type : {et}")

            #Ajout de tri de liste car modalité et calcul d'occurence inexacte sans
                if not liste_est_triee(liste_courante):
                    print("Liste non triée\n Tri en cours...")
                    liste_courante = liste_tri_selection_minimum(liste_courante)
                    
                med = mediane(liste_courante)
                mod = modalites(liste_courante)

                print(f"- Médiane : {med}")
                print(f"- Modalités : {mod}")

        elif choix == "4":
            if len(liste_courante) == 0:
                print("Aucune donnée chargée, impossible de faire une recherche.")
            else:
                prix_recherche = int(input("Entrez un prix à rechercher dans la liste : "))
                occ = nombre_occurrence(prix_recherche, liste_courante)
                if occ == -1:
                    print(f"Aucune occurrence de la valeur {prix_recherche} trouvée.")
                else:
                    print(f"Résultats pour le prix {prix_recherche} :")
                    print(f"- Nombre d'occurrences : {occ}")
            
        elif choix == "5":
            print("Programme terminé.")
            terminer = True
        else:
            print("Choix invalide, veuillez réessayer.")
analyseur()
