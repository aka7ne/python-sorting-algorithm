#Kawthar Bouguima Fichier test n°5 Calcul du maximum des valeurs d'une liste
from KB_02_listes_type import *


print("*** Test 1 : Liste une seule valeur ***")
ltrf = [tarif_train("Paris", "Lyon", 50)]
resultat_fonction = (tarif_maximum(ltrf))
print(f"Le tarif maximum est de : {resultat_fonction} €")


print("\n*** Test 2: Maximum au début ***")
ltrf = [tarif_train("Lyon", "Marseille", 80),
    tarif_train("Bordeaux", "Toulouse", 30),
    tarif_train("Nice", "Lille", 45)]
resultat_fonction = (tarif_maximum(ltrf))
print(f"Le tarif maximum est de : {resultat_fonction} €")

print("\n*** Test 3 : Valeurs identiques ***")
ltrf = [tarif_train("Paris", "Lyon", 40),
        tarif_train("Paris", "Nice", 40),
        tarif_train("Paris", "Marseille", 40)]
resultat_fonction = (tarif_maximum(ltrf))
print(f"Le tarif maximum est de : {resultat_fonction} €")

print("\n*** Test 4: Maximum n'importe ou ***")
ltrf = [tarif_train("Crest", "Paris Gare de Lyon", 36),
    tarif_train("Les Aubrais", "Narbonne", 49),
    tarif_train("Caussade Tarn-et-Garonne", "Paris Gare de Lyon", 20),
    tarif_train("Mérens-les-Vals", "Les Aubrais", 185),
    tarif_train("Cransac", "Paris Bercy", 59),]
resultat_fonction = (tarif_maximum(ltrf))
print(f"Le tarif maximum est de : {resultat_fonction} €")

print("\n*** Test 5: Maximum a la fin ***")
ltrf = [tarif_train("Gramat", "Paris Austerlitz", 67),
    tarif_train("Saint-Christophe", "Les Aubrais", 39),
    tarif_train("Assier", "Les Aubrais", 169),
    tarif_train("Laroquebrou", "Paris Austerlitz", 12),
    tarif_train("Cransac", "Paris Gare de Lyon", 201)]
resultat_fonction = (tarif_maximum(ltrf))
print(f"Le tarif maximum est de : {resultat_fonction} €")
        
