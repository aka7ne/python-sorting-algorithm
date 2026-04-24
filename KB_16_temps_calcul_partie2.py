#Kawthar Bouguima TP PROJET partie 2 du 19/04/2025
"""
Ce fichier contient une fonction de calcul de temps linéaire pour les fonctions :
- vérification de tri
- tri par selection du minimum
- calcul de médiane
- calcul de modalités
ainsi que les courbes dessinées correspondantes.
"""

from KB_02_listes_type import *
from outils_dessin import *
from outils_mesure import *

nb_repet = 50

instructions_liste_est_triee_setup = """
from KB_02_listes_type import liste_est_triee
from __main__ import ltrf
"""
instructions_liste_est_triee_stmt = """
tot = liste_est_triee(ltrf)
"""

instructions_liste_tri_selection_minimum_setup = """
from KB_02_listes_type import liste_tri_selection_minimum
from __main__ import ltrf
"""
instructions_liste_tri_selection_minimum_stmt = """
tot1 = liste_tri_selection_minimum (ltrf)
"""

instructions_modalites_setup = """
from KB_02_listes_type import modalites
from __main__ import ltrf
"""
instructions_modalites_stmt = """
tot2 = modalites(ltrf)
"""

instructions_mediane_setup = """
from KB_02_listes_type import mediane
from __main__ import ltrf
"""
instructions_mediane_stmt = """
tot3 = mediane(ltrf)
"""

longueur_max = 300
pas_longueur = longueur_max//100

courbe_liste_est_triee = []
courbe_liste_tri_selection_minimum = []
courbe_mediane = []
courbe_modalites = []
courbe_constante = []
courbe_constante_2 = []

k = 50
for longueur in range(0, longueur_max + 1, pas_longueur):
    courbe_constante.append((longueur, k * (longueur ** 2)))

k = 100
for longueur in range(0, longueur_max + 1, pas_longueur):
    courbe_constante_2.append((longueur, k * longueur))

for longueur in range(0, longueur_max + 1, pas_longueur):
    ltrf = []
    for n in range(longueur):
        ltrf.append(tarif_train("Montpellier", "Paris", 52))

    if longueur > 0:
        t_triee = timeit.timeit(stmt=instructions_liste_est_triee_stmt,
                            setup=instructions_liste_est_triee_setup,
                            number=nb_repet)
        t_triee = temps_en_nanoseconde(t_triee / nb_repet)
        courbe_liste_est_triee.append((longueur, t_triee))

        t_tri = timeit.timeit(stmt=instructions_liste_tri_selection_minimum_stmt,
                          setup=instructions_liste_tri_selection_minimum_setup,
                          number=nb_repet)
        t_tri = temps_en_nanoseconde(t_tri / nb_repet)
        courbe_liste_tri_selection_minimum.append((longueur, t_tri))


        t_mediane = timeit.timeit(stmt=instructions_mediane_stmt,
                              setup=instructions_mediane_setup,
                              number=nb_repet)
        t_mediane = temps_en_nanoseconde(t_mediane / nb_repet)
        courbe_mediane.append((longueur, t_mediane))

        t_modalites = timeit.timeit(stmt=instructions_modalites_stmt,
                                setup=instructions_modalites_setup,
                                number=nb_repet)
        t_modalites = temps_en_nanoseconde(t_modalites / nb_repet)
        courbe_modalites.append((longueur, t_modalites))


print("\n¤ Légende des courbes :")
print("- Bleu   : fonction de tri (tri par sélection minimum)")

dessine_lignes_brisees(
    courbe_bleue=courbe_liste_tri_selection_minimum,
    courbe_violet=courbe_constante
)
print("\n¤ Légende des courbes :")
print("- Rouge  : fonction de tri (vérification tri)")
print("- Vert   : fonction de médiane")
print("- Orange : fonction de modalités")
print("- Violet : courbe de référence (constante)")

dessine_lignes_brisees(
    courbe_rouge=courbe_liste_est_triee,
    courbe_verte=courbe_mediane,
    courbe_orange=courbe_modalites,
    courbe_violet = courbe_constante_2
)
