#Kawthar Bouguima Fichier test n°4 Calcul du minimum des valeurs d'une liste
from KB_02_listes_type import *


print("*** Test 1: Liste une seule valeur***")
ltrf = [tarif_train("Lyon", "Marseille", 50)]
resultat_fonction = (tarif_minimum(ltrf))
print(f"Le tarif minimum est de : {resultat_fonction} €")

print("\n*** Test 2: Minimum au début ***")
ltrf = [tarif_train("Bordeaux", "Toulouse", 30),
        tarif_train("Lyon", "Marseille", 50),
        tarif_train("Nice", "Lille", 45)]
resultat_fonction = (tarif_minimum(ltrf))
print(f"Le tarif minimum est de : {resultat_fonction} €")

print("\n*** Test 3 : liste valeurs identiques ***")
ltrf = [tarif_train("Paris", "Lyon", 40),
        tarif_train("Paris", "Nice", 40),
        tarif_train("Paris", "Marseille", 40)]
resultat_fonction = (tarif_minimum(ltrf))
print(f"Le tarif minimum est de : {resultat_fonction} €")

print("\n*** Test 4: Minimum a la fin***")
ltrf = [tarif_train("Crest", "Paris Gare de Lyon", 36),
    tarif_train("Les Aubrais", "Narbonne", 49),
    tarif_train("Caussade Tarn-et-Garonne", "Paris Gare de Lyon", 20),
    tarif_train("Saint-Christophe", "Paris Bercy", 21),
    tarif_train("Mérens-les-Vals", "Les Aubrais", 185),
    tarif_train("Laroquebrou", "Paris Austerlitz", 12)]
resultat_fonction = (tarif_minimum(ltrf))
print(f"Le tarif minimum est de : {resultat_fonction} €")

print("\n*** Test 4: Minimum n'importe ou ***")
ltrf = [tarif_train("Crest", "Paris Gare de Lyon", 36),
    tarif_train("Les Aubrais", "Narbonne", 49),
    tarif_train("Caussade Tarn-et-Garonne", "Paris Gare de Lyon", 20),
    tarif_train("Mérens-les-Vals", "Les Aubrais", 185),
    tarif_train("Cransac", "Paris Bercy", 59),]
resultat_fonction = (tarif_minimum(ltrf))
print(f"Le tarif minimum est de : {resultat_fonction} €")
