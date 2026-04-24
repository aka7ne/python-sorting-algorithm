#Kawthar Bouguima test n°10 fonction de tri par sélection du minimum

from KB_02_listes_type import *

print("*** Test 1: Liste non triée ***")
ltrf = [tarif_train("Lyon", "Marseille", 50),
    tarif_train("Bordeaux", "Toulouse", 30),
    tarif_train("Nice", "Lille", 45),
    tarif_train("Cransac", "Paris Gare de Lyon", 201),
    tarif_train("Tarascon-sur-Ariège", "Les Aubrais", 77)]

longueur_avant = len(ltrf)
ltrf = liste_tri_selection_minimum(ltrf)
affiche_liste_tarif(ltrf)
print("Est ce que le tri est bon ? ", liste_est_triee (ltrf))
print("Nombre d'éléments est conservé ?", len(ltrf) == longueur_avant)


print("\n*** Test 2: Liste déjà triée ***")
ltrf = [tarif_train("Paris Austerlitz", "Rodez", 28),
        tarif_train("Bordeaux", "Toulouse", 30),
        tarif_train("Nice", "Lille", 45),
        tarif_train("Lyon", "Marseille", 50)]

longueur_avant = len(ltrf)
ltrf = liste_tri_selection_minimum(ltrf)
affiche_liste_tarif(ltrf)
print("Est ce que le tri est bon ? ", liste_est_triee (ltrf))
print("Nombre d'éléments est conservé ?", len(ltrf) == longueur_avant)

print("\n*** Test 3 : liste un seul élément ***")
ltrf = [tarif_train("Paris", "Marseille", 40)]

longueur_avant = len(ltrf)
liste_tri_selection_minimum(ltrf)
affiche_liste_tarif(liste_tri_selection_minimum(ltrf))

print("Est-ce que le tri est bon ?", liste_est_triee(ltrf))
print("Nombre d'éléments est conservé ?", len(ltrf) == longueur_avant)
    
print("\n*** Test 4 : liste valeurs identiques ***")
ltrf = [tarif_train("Paris", "Lyon", 40),
        tarif_train("Paris", "Nice", 40),
        tarif_train("Paris", "Marseille", 40)]

longueur_avant = len(ltrf)
ltrf = liste_tri_selection_minimum(ltrf)
affiche_liste_tarif(ltrf)
print("Est ce que le tri est bon ? ", liste_est_triee (ltrf))
print("Nombre d'éléments est conservé ?", len(ltrf) == longueur_avant)

