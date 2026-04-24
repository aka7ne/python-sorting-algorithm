#Kawthar Bouguima Fichier test n°2 affichage de liste

from KB_02_listes_type import *

print("*** Test 1 : Liste vide ***")
liste_vide = []
affiche_liste_tarif(liste_vide)


print("\n*** Test 2 : Liste a 1 élément ***")
liste_1_element = [tarif_train("Paris", "Montpellier", 20)]
affiche_liste_tarif(liste_1_element)



print("\n*** Test 3 : Liste a plusieurs éléments ***")
liste_plusieurs_element =  [tarif_train("Lyon", "Marseille", 50),
    tarif_train("Bordeaux", "Toulouse", 30),
    tarif_train("Nice", "Lille", 45)]
affiche_liste_tarif (liste_plusieurs_element)

