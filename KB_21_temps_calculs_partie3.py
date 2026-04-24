#Kawthar Bouguima TP PROJET partie 2 du 26/04/2025
"""
Ce fichier contient une fonction de calcul de temps logarithmique pour les fonctions :
- Recherche dichotomique quelconque
- Recherche dichotomique plus petit indice
- Recherche dichotomique plus grand indice
- Nombres d'occurrences
ainsi que les courbes dessinées correspondantes.
"""

from KB_02_listes_type import *
from outils_dessin import *
from outils_mesure import *
import math

nb_repet = 100

instructions_recherche_dichotomique_setup = """
from KB_02_listes_type import recherche_dichotomique
from __main__ import ltrf
"""
instructions_recherche_dichotomique_stmt = """
tot = recherche_dichotomique(777, ltrf)
"""

instructions_plus_petit_indice_setup = """
from KB_02_listes_type import plus_petit_indice
from __main__ import ltrf
"""
instructions_plus_petit_indice_stmt = """
tot1 = plus_petit_indice(777, ltrf)
"""

instructions_plus_grand_indice_setup = """
from KB_02_listes_type import plus_grand_indice
from __main__ import ltrf
"""
instructions_plus_grand_indice_stmt = """
tot2 = plus_grand_indice (777, ltrf)
"""

instructions_nombre_occurrence_setup = """
from KB_02_listes_type import nombre_occurrence
from __main__ import ltrf
"""
instructions_nombre_occurrence_stmt = """
tot3 = nombre_occurrence(777, ltrf)
"""

longueur_max = 1000
pas_longueur = longueur_max//100

courbe_recherche_dichotomique = []
courbe_plus_petit_indice= []
courbe_plus_grand_indice = []
courbe_nombre_occurrence = []
courbe_constante = []

k = 500
for longueur in range(1, longueur_max + 1, pas_longueur):
    courbe_constante.append((longueur, k * math.log(longueur)))#math.log afin de faire une constante de complexité logarithmique

for longueur in range(0, longueur_max+1, pas_longueur):
    ltrf = []
    for n in range(longueur):
        ltrf.append(tarif_train("Montpellier", "Paris", n))
        
    ltrf = liste_tri_selection_minimum(ltrf)

    t_dic = timeit.timeit(stmt=instructions_recherche_dichotomique_stmt,
                            setup=instructions_recherche_dichotomique_setup,
                            number=nb_repet)
    t_dic = temps_en_nanoseconde(t_dic / nb_repet)
    courbe_recherche_dichotomique.append((longueur, t_dic))
    

    t_petit = timeit.timeit(stmt=instructions_plus_petit_indice_stmt,
                          setup=instructions_plus_petit_indice_setup,
                          number=nb_repet)
    t_petit = temps_en_nanoseconde(t_petit / nb_repet)
    courbe_plus_petit_indice.append((longueur, t_petit))


    t_grand = timeit.timeit(stmt=instructions_plus_grand_indice_stmt,
                              setup=instructions_plus_grand_indice_setup,
                              number=nb_repet)
    t_grand = temps_en_nanoseconde(t_grand / nb_repet)
    courbe_plus_grand_indice.append((longueur, t_grand))

    t_occ = timeit.timeit(stmt=instructions_nombre_occurrence_stmt,
                                setup=instructions_nombre_occurrence_setup,
                                number=nb_repet)
    t_occ = temps_en_nanoseconde(t_occ / nb_repet)
    courbe_nombre_occurrence.append((longueur, t_occ))


print("\n¤ Légende des courbes :")
print("- Rouge  : Recherche dichotomique quelconque")
print("- Bleu   : Recherche dichotomique plus petit indice")
print("- Vert   : Recherche dichotomique plus grand indice")
print("- Orange : Nombres d'occurrences")
print("- Violet : courbe de référence (constante)")

dessine_lignes_brisees(
    courbe_rouge = courbe_recherche_dichotomique,
    courbe_bleue = courbe_plus_petit_indice,
    courbe_verte = courbe_plus_grand_indice,
    courbe_orange = courbe_nombre_occurrence,
    courbe_violet = courbe_constante
)
