#Kawthar Bouguima test n°12 calcul de modalité
from KB_02_listes_type import *


print("\n*** Test 1: Même valeur ***")
ltrf = [tarif_train("Paris", "Lyon", 40),
        tarif_train("Paris", "Lyon", 40),
        tarif_train("Paris", "Lyon", 40),
        tarif_train("Paris", "Lyon", 40),
        tarif_train("Paris", "Lyon", 40)]

print ("Les modalités sont :",modalites(ltrf))
print("Nombre de modalités :", len(modalites(ltrf)))

print("\n*** Test 2: Aucune même valeur ***")
ltrf = [tarif_train("Avignon", "Tours", 35),
        tarif_train("Dijon", "Metz", 45),
        tarif_train("Reims", "Rouen", 50),
        tarif_train("Brest", "Grenoble", 55),
        tarif_train("Nantes", "Strasbourg", 60)]
print ("Les modalités sont :",modalites(ltrf))
print("Nombre de modalités :", len(modalites(ltrf)))

print("\n*** Test 3 : Cas général ***")
ltrf = [tarif_train("Lille", "Paris", 30),
        tarif_train("Lille", "Paris", 30),
        tarif_train("Toulouse", "Bordeaux", 45),
        tarif_train("Lyon", "Nice", 55),
        tarif_train("Lyon", "Nice", 55)]
print ("Les modalités sont :",modalites(ltrf))
print("Nombre de modalités :", len(modalites(ltrf)))
