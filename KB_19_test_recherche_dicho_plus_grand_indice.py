#Kawthar Bouguima fichier test n°14 de recherche dichotomique du plus grand indice sur liste triée
from KB_02_listes_type import *

print("*** Test recherche dernier indice valeur multiple:***")
ltrf = [
    tarif_train("Paris", "Lyon", 45),
    tarif_train("Lyon", "Nice", 50),
    tarif_train("Dijon", "Grenoble", 55),
    tarif_train("Lille", "Toulouse", 60),
    tarif_train("Bordeaux", "Marseille", 60),
    tarif_train("Metz", "Strasbourg", 60),
    tarif_train("Amiens", "Nantes", 65),
    tarif_train("Tours", "Besançon", 70),
    tarif_train("Limoges", "Clermont", 75),
    tarif_train("Caen", "Rennes", 80),
    tarif_train("Rouen", "Nancy", 85)
]
print("Valeur recherchée : 60 |  Le dernier indice est :", plus_grand_indice(60, ltrf))

print("\n*** Test recherche dernier indice valeur multiple: ***")
ltrf = [
    tarif_train("Nîmes", "Avignon", 25),
    tarif_train("Bordeaux", "Paris", 30),
    tarif_train("Grenoble", "Toulouse", 35),
    tarif_train("Lyon", "Marseille", 40),
    tarif_train("Nice", "Lille", 40),
    tarif_train("Dunkerque", "Caen", 40),
    tarif_train("Angers", "Reims", 45),
    tarif_train("Poitiers", "Le Mans", 50),
    tarif_train("Orléans", "Mulhouse", 55),
    tarif_train("Versailles", "Troyes", 60)
]
print("Valeur recherchée : 40 |  Le dernier indice est :", plus_grand_indice(40, ltrf))  

print("\n*** Test recherche dernier indice valeur absente: ***")
ltrf = [
    tarif_train("Montpellier", "Perpignan", 35),
    tarif_train("Marseille", "Lyon", 40),
    tarif_train("Nice", "Grenoble", 45),
    tarif_train("Toulouse", "Nantes", 50),
    tarif_train("Strasbourg", "Metz", 55),
    tarif_train("Paris", "Bordeaux", 60),
    tarif_train("Rouen", "Caen", 65),
    tarif_train("Nancy", "Besançon", 70),
    tarif_train("Dijon", "Lille", 75),
    tarif_train("Amiens", "Reims", 80)
]
print("Valeur recherchée : 30 | Le dernier indice est :", plus_grand_indice(30, ltrf))  
