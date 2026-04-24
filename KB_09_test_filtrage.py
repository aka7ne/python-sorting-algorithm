#Kawthar Bouguima Fichier test n°8 fonction filtrage
from KB_02_listes_type import *

print("\n*** Test 1 : Liste a plusieurs éléments ***\n")
ltrf = [
    tarif_train("Lyon", "Paris", 45),
    tarif_train("Marseille", "Lyon", 60),
    tarif_train("Lyon", "Grenoble", 30),
    tarif_train("Paris", "Lyon", 75)
]

print("=== Tarifs depuis Lyon ===")
tarifs_depuis_lyon = filtrage(ltrf, "Lyon", "origine")
affiche_liste_tarif(tarifs_depuis_lyon)

print("\n=== Tarifs vers Lyon ===")
tarifs_vers_lyon = filtrage(ltrf, "Lyon", "destination")
affiche_liste_tarif(tarifs_vers_lyon)

print("\n*** Test 2 : Liste a 1 seules valeur ***")

ltrf = [tarif_train("Lyon", "Grenoble", 30)]

print("=== Tarifs depuis Lyon ===")
tarifs_depuis_lyon = filtrage(ltrf, "Lyon", "origine")
affiche_liste_tarif(tarifs_depuis_lyon)

print("\n=== Tarifs vers Lyon ===")
tarifs_vers_lyon = filtrage(ltrf, "Lyon", "destination")
affiche_liste_tarif(tarifs_vers_lyon)

print("\n*** Test 2 : Liste avec donnée absente ***")

ltrf = [tarif_train("Marseille", "Toulouse", 35),
    tarif_train("Nantes", "Strasbourg", 45),
    tarif_train("Bordeaux", "Paris", 55),
    tarif_train("Toulouse", "Grenoble", 65)]

print("=== Tarifs depuis Lyon ===")
tarifs_depuis_lyon = filtrage(ltrf, "Lyon", "origine")
affiche_liste_tarif(tarifs_depuis_lyon)

print("\n=== Tarifs vers Lyon ===")
tarifs_vers_lyon = filtrage(ltrf, "Lyon", "destination")
affiche_liste_tarif(tarifs_vers_lyon)
