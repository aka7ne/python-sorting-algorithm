#Kawthar Bouguima fichier test n°15 calcul du nombre d'occurences d'une valeurs
from KB_02_listes_type import *

print("*** Test 1 : Une seule valeur ***")
ltrf = [
    tarif_train("Paris", "Lyon", 10),
    tarif_train("Lille", "Nice", 15),
    tarif_train("Dijon", "Reims", 20),
    tarif_train("Tours", "Nancy", 25),
    tarif_train("Amiens", "Grenoble", 30),
    tarif_train("Rouen", "Caen", 35),
    tarif_train("Strasbourg", "Orléans", 40),
    tarif_train("Brest", "Metz", 45),
    tarif_train("Marseille", "Toulouse", 50),
    tarif_train("Nantes", "Strasbourg", 55),
    tarif_train("Bordeaux", "Lille", 60)]
print("Valeur recherchée : 40 | Nombre d'occurrences :", nombre_occurrence(40, ltrf))  

print("\n*** Test 2 : Valeur présente plusieurs fois ***")
ltrf = [
    tarif_train("Paris", "Lyon", 10),
    tarif_train("Lille", "Nice", 20),
    tarif_train("Dijon", "Reims", 30),
    tarif_train("Tours", "Nancy", 30),
    tarif_train("Amiens", "Grenoble", 30),
    tarif_train("Rouen", "Caen", 35),
    tarif_train("Strasbourg", "Orléans", 40),
    tarif_train("Brest", "Metz", 45),
    tarif_train("Marseille", "Toulouse", 50),
    tarif_train("Nantes", "Strasbourg", 55),
    tarif_train("Bordeaux", "Lille", 60),
    tarif_train("Toulon", "Perpignan", 65),
    tarif_train("Annecy", "Poitiers", 70)]
print("Valeur recherchée : 30 | Nombre d'occurrences :", nombre_occurrence(30, ltrf))

print("\n*** Test 3 : Valeur absente ***")
ltrf = [
    tarif_train("Paris", "Lyon", 10),
    tarif_train("Lille", "Nice", 15),
    tarif_train("Dijon", "Reims", 20),
    tarif_train("Tours", "Nancy", 25),
    tarif_train("Amiens", "Grenoble", 30),
    tarif_train("Strasbourg", "Orléans", 40),
    tarif_train("Brest", "Metz", 45),
    tarif_train("Marseille", "Toulouse", 50),
    tarif_train("Nantes", "Strasbourg", 55),
    tarif_train("Bordeaux", "Lille", 60),
    tarif_train("Toulon", "Perpignan", 65)]
print("Valeur recherchée : 35 |Nombre d'occurrences :", nombre_occurrence(35, ltrf))

print("\n*** Test 4 : Liste a un élément ***")
ltrf = [tarif_train("Bordeaux", "Lille", 30)]
print("Valeur recherchée : 30 | Nombre d'occurrences :", nombre_occurrence(30, ltrf))  

print("\n*** Test 5 : Valeur petit et plus grand indice ***")
ltrf = [
    tarif_train("Paris", "Lyon", 10),
    tarif_train("Bordeaux", "Nice", 20),
    tarif_train("Lille", "Toulouse", 30),
    tarif_train("Lyon", "Marseille", 30),
    tarif_train("Nice", "Toulouse", 30),
    tarif_train("Lyon", "Marseille", 30),
    tarif_train("Nantes", "Grenoble", 40),
    tarif_train("Toulouse", "Paris", 50),
    tarif_train("Nantes", "Strasbourg", 55),
    tarif_train("Bordeaux", "Lille", 60),
    tarif_train("Toulon", "Perpignan", 65)
]
print("Valeur recherchée : 30 | Nombre d'occurrences :", nombre_occurrence(30, ltrf))

print("\n*** Test 6 : Valeurs identiques ***")
ltrf = [
    tarif_train("Paris", "Lyon", 25),
    tarif_train("Marseille", "Nice", 25),
    tarif_train("Toulouse", "Bordeaux", 25),
    tarif_train("Lille", "Strasbourg", 25),
    tarif_train("Nantes", "Rennes", 25),
    tarif_train("Grenoble", "Dijon", 25),
    tarif_train("Rouen", "Amiens", 25),
    tarif_train("Reims", "Orléans", 25),
    tarif_train("Caen", "Nancy", 25),
    tarif_train("Poitiers", "Angers", 25),
    tarif_train("Perpignan", "Clermont-Ferrand", 25),
    tarif_train("Troyes", "Besançon", 25)
]
print("Valeur recherchée : 25 | Nombre d'occurrences :", nombre_occurrence(25, ltrf))
