#Kawthar Bouguima TP PROJET partie 1 du 7/03/2025
"""
- Ce fichier contient une déclaration d'un nouveau type de données ainsi
qu'une foncion permettant d'afficher une instance de mon type tarifT
- Source : Cours ainsi que correction des TP

"""
from dataclasses import dataclass

@dataclass
class tarif_train() :
          """
          gare_origine : chaîne de caractères (str)
          gare_destinataire : chaîne de caractères (str)
          prix : entier (int)
          """
          gOrigine : str
          gDestinataire : str
          prix : int

def affiche_tarif( trf ):
    """
    Rôle : affiche les informations de tarif
    Donnée : trf : objet de type tarif_train
    Préconditions : trf doit être un objet de type tarif_train.
    """
    print("Gare d'origine:",trf.gOrigine, " Gare destinataire :" ,trf.gDestinataire, " Prix minimum: ",trf.prix ,"€" )
