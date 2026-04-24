#Kawthar Bouguima fichier test n°9 Vérifie si une liste est trié ou non (True , False)
from KB_02_listes_type import *

print("\n*** Test 1: Liste un élément ***")
ltrf= [tarif_train("Paris", "Montpellier", 20)]
print("Cette liste est triée ? ", liste_est_triee (ltrf))


print("\n*** Test 2: Liste triée ***")
ltrf = [tarif_train("Bordeaux", "Toulouse", 30),
        tarif_train("Nice", "Lille", 45),
        tarif_train("Lyon", "Marseille", 50)]
print("Cette liste est triée ? ", liste_est_triee (ltrf))


print("\n*** Test 3: Liste non triée ***")
ltrf= [tarif_train("Lyon", "Marseille", 50),
    tarif_train("Bordeaux", "Toulouse", 30),
    tarif_train("Nice", "Lille", 45)]
print("Cette liste est triée ? ", liste_est_triee (ltrf))

print("\n*** Test 4 : Liste valeurs identiques ***")
ltrf = [tarif_train("Paris", "Lyon", 40),
        tarif_train("Paris", "Nice", 40),
        tarif_train("Paris", "Marseille", 40)]
print("Résultat obtenu :", liste_est_triee(ltrf))


