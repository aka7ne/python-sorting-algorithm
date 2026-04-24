#Kawthar Bouguima fichier test n°13 Recherche dichotomique du plus petit indice sur liste triée
from KB_02_listes_type import *

print("***Test recherche premier indice valeur multiple:***")
ltrf = [
    tarif_train("Paris", "Lyon", 40),
    tarif_train("Lyon", "Nice", 40),
    tarif_train("Marseille", "Toulouse", 50),
    tarif_train("Nantes", "Strasbourg", 60),
    tarif_train("Bordeaux", "Reims", 70),
    tarif_train("Toulouse", "Grenoble", 70),
    tarif_train("Dijon", "Metz", 70),
    tarif_train("Nancy", "Tours", 80),
    tarif_train("Caen", "Limoges", 90),
    tarif_train("Orléans", "Amiens", 100)
]
print("Valeur recherchée : 70 |  Le premier indice est :", plus_petit_indice(70, ltrf))

print("\n*** Test recherche premier indice valeur multiple: ***")
ltrf = [
    tarif_train("Lille", "Paris", 25),
    tarif_train("Nice", "Lyon", 30),
    tarif_train("Lyon", "Nice", 35),
    tarif_train("Marseille", "Toulouse", 40),
    tarif_train("Strasbourg", "Nantes", 40),
    tarif_train("Bordeaux", "Paris", 40),
    tarif_train("Toulouse", "Grenoble", 45),
    tarif_train("Dijon", "Reims", 50),
    tarif_train("Rennes", "Metz", 55),
    tarif_train("Nancy", "Tours", 60)
]
print("Valeur recherchée : 40 |  Le premier indice est :", plus_petit_indice(40, ltrf))  


print("\n*** Test recherche premier indice valeur absente: ***")
ltrf = [
   tarif_train("Paris", "Lyon", 20),
    tarif_train("Lyon", "Nice", 30),
    tarif_train("Marseille", "Toulouse", 40),
    tarif_train("Nantes", "Strasbourg", 50),
    tarif_train("Bordeaux", "Paris", 60),
    tarif_train("Toulouse", "Grenoble", 70),
    tarif_train("Dijon", "Reims", 80),
    tarif_train("Rennes", "Metz", 90),
    tarif_train("Nancy", "Tours", 100),
    tarif_train("Caen", "Limoges", 110)
]
print("Valeur recherchée : 45 | Le premier indice est :", plus_petit_indice(45, ltrf))  
