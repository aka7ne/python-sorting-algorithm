#Kawthar Bouguima TP PROJET partie 1 du 01/04/2025
"""
Ce fichier contient une fonction de calcul de temps linéaire pour les fonctions :
- Calcul de minimum
- Calcul de maximum
_ Calcul de moyenne
- Calcul d'écart-type
ainsi que les courbes dessinées correspondantes 
"""

from KB_02_listes_type import *
from outils_dessin import *
from outils_mesure import *
import random

nb_repet = 100

instructions_minimum_setup ="""
from KB_02_listes_type import tarif_minimum
from __main__ import ltrf
"""
instructions_minimum_stmt = """
tarif_minimum(ltrf)
"""

instructions_maximum_setup = """
from KB_02_listes_type import tarif_maximum
from __main__ import ltrf
"""
instructions_maximum_stmt = """
tarif_maximum(ltrf)
"""

instructions_moyenne_setup = """
from KB_02_listes_type import tarif_moyenne
from __main__ import ltrf
"""
instructions_moyenne_stmt = """
tarif_moyenne(ltrf)
"""

instructions_ecart_setup = """
from KB_02_listes_type import ecart_type
from __main__ import ltrf
"""
instructions_ecart_stmt = "ecart_type(ltrf)"

longueur_max = 1000
pas_longueur = longueur_max//100

courbe_minimum = []
courbe_maximum = []
courbe_moyenne = []
courbe_ecart = []
courbe_constante = []

k = 100
for longueur in range(0, longueur_max + 1, pas_longueur):
    courbe_constante.append((longueur, k * longueur))


for longueur in range(0, longueur_max+1, pas_longueur):
    ltrf = []
    for n in range(longueur):
        prix_aleatoire = random.randint(20, 200)
        ltrf.append(tarif_train("Montpellier", "Paris", prix_aleatoire))

    if longueur > 0:

        t_min = timeit.timeit(stmt=instructions_minimum_stmt,
                   setup=instructions_minimum_setup,
                   number=nb_repet)
        t_min = temps_en_nanoseconde(t_min / nb_repet)
        courbe_minimum.append((longueur, t_min))

        t_max = timeit.timeit(stmt=instructions_maximum_stmt,
                          setup=instructions_maximum_setup,
                          number=nb_repet)
        t_max = temps_en_nanoseconde(t_max / nb_repet)
        courbe_maximum.append((longueur, t_max))


        t_moy = timeit.timeit(stmt=instructions_moyenne_stmt,
                          setup=instructions_moyenne_setup,
                          number=nb_repet)
        t_moy = temps_en_nanoseconde(t_moy / nb_repet)
        courbe_moyenne.append((longueur, t_moy))

        t_ecart = timeit.timeit(stmt=instructions_ecart_stmt,
                            setup=instructions_ecart_setup,
                            number=nb_repet)
        t_ecart = temps_en_nanoseconde(t_ecart / nb_repet)
        courbe_ecart.append((longueur, t_ecart))


print("\n¤ Légende des courbes :")
print("- Rouge  : fonction de calcul de minimum ")
print("- Bleu   : fonction de calcul de maximum")
print("- Vert   : fonction de calcul de moyenne")
print("- Orange : fonction de calcul d'écart-type")
print("- Violet : courbe de référence (constante)")

dessine_lignes_brisees(
    courbe_rouge=courbe_minimum,
    courbe_bleue=courbe_maximum,
    courbe_verte=courbe_moyenne,
    courbe_orange=courbe_ecart,
    courbe_violet=courbe_constante)
