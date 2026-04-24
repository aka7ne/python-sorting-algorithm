#Kawthar Bouguima fichier test n°12 Recherche dichotomique quelconque sur liste triée 

from KB_02_listes_type import *

print("*** Test recherche dichotomique valeur au début: ***")
ltrf= [  tarif_train("Lille", "Paris", 20),
    tarif_train("Nice", "Lyon", 25),
    tarif_train("Lyon", "Nice", 30),
    tarif_train("Marseille", "Toulouse", 35),
    tarif_train("Strasbourg", "Nantes", 40),
    tarif_train("Bordeaux", "Paris", 45),
    tarif_train("Toulouse", "Grenoble", 50),
    tarif_train("Dijon", "Reims", 55),
    tarif_train("Rennes", "Metz", 60),
    tarif_train("Nancy", "Tours", 65)
]
print("Valeur recherchée : 20 | L'indice est :", recherche_dichotomique(20, ltrf))

print("\n*** Test recherche dichotomique valeur fin: ***")
ltrf= [ tarif_train("Lille", "Paris", 22),
    tarif_train("Nice", "Lyon", 28),
    tarif_train("Lyon", "Nice", 33),
    tarif_train("Marseille", "Toulouse", 39),
    tarif_train("Strasbourg", "Nantes", 43),
    tarif_train("Bordeaux", "Paris", 47),
    tarif_train("Toulouse", "Grenoble", 52),
    tarif_train("Dijon", "Reims", 58),
    tarif_train("Rennes", "Metz", 65),
    tarif_train("Nancy", "Tours", 70)]
print("Valeur recherchée : 70 | L'indice est :",recherche_dichotomique(70, ltrf))

print("\n*** Test recherche dichotomique valeur n'importe où: ***")
ltrf= [tarif_train("Lille", "Paris", 15),
    tarif_train("Nice", "Lyon", 20),
    tarif_train("Lyon", "Nice", 25),
    tarif_train("Marseille", "Toulouse", 30),
    tarif_train("Strasbourg", "Nantes", 35),
    tarif_train("Bordeaux", "Paris", 40),
    tarif_train("Toulouse", "Grenoble", 45),
    tarif_train("Dijon", "Reims", 50),
    tarif_train("Rennes", "Metz", 55),]
print("Valeur recherchée : 40 | L'indice est :", recherche_dichotomique(40, ltrf))

print("\n*** Test recherche dichotomique mauvaise valeur: ***")
ltrf= [    tarif_train("Lille", "Paris", 10),
    tarif_train("Nice", "Lyon", 15),
    tarif_train("Lyon", "Nice", 20),
    tarif_train("Marseille", "Toulouse", 25),
    tarif_train("Strasbourg", "Nantes", 30),
    tarif_train("Bordeaux", "Paris", 35),
    tarif_train("Toulouse", "Grenoble", 40),
    tarif_train("Dijon", "Reims", 45),
    tarif_train("Rennes", "Metz", 50),
    tarif_train("Nancy", "Tours", 55)]
print("Valeur recherchée : 22 | L'indice est :", recherche_dichotomique(22, ltrf))
