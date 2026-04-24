#Kawthar Bouguima Fichier test n°6 Calcul de la moyenne des valeurs d'une liste
from KB_02_listes_type import *

print("*** Test 1 : Liste une seule valeur ***")
ltrf = [tarif_train("Paris", "Lyon", 50)]
resultat_fonction = (tarif_moyenne(ltrf))
print(f"Le tarif moyen est de : {resultat_fonction} €")
print("Moyenne attendue : 50")

print("\n*** Test 2 : Petite liste valeurs simples ***")
ltrf = [tarif_train("Paris", "Lyon", 10),
        tarif_train("Paris", "Nice", 20),
        tarif_train("Paris", "Marseille", 30)]
resultat_fonction = (tarif_moyenne(ltrf))
print(f"Le tarif moyen est de : {resultat_fonction} €")
print("Moyenne attendue : 20")

print("\n*** Test 3: Petite liste ***")
ltrf = [tarif_train("Lyon", "Marseille", 57),
    tarif_train("Bordeaux", "Toulouse", 30),
    tarif_train("Nice", "Lille", 45)]
resultat_fonction = (tarif_moyenne(ltrf))
print(f"Le tarif moyen est de : {resultat_fonction} €")
print("Moyenne attendue : 44")

print("\n*** Test 4 : Valeurs identiques ***")
ltrf = [tarif_train("Paris", "Lyon", 40),
        tarif_train("Paris", "Nice", 40),
        tarif_train("Paris", "Marseille", 40)]
resultat_fonction = (tarif_moyenne(ltrf))
print(f"Le tarif moyen est de : {resultat_fonction} €")
print("Moyenne attendue : 40")

