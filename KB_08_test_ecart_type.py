#Kawthar Bouguima Fichier test n°7 Calcul l'écart-type des valeurs d'une liste
from KB_02_listes_type import *

print("*** Test 1: Petite liste ***")
ltrf = [tarif_train("Bordeaux", "Toulouse", 30)]
resultat_fonction = (ecart_type(ltrf))
print(f"L'écart type est de : {resultat_fonction} €")

print("\n*** Test 2 : Valeurs identiques ***")
ltrf = [
    tarif_train("Paris", "Lyon", 50),
    tarif_train("Marseille", "Bordeaux", 50),
    tarif_train("Nice", "Toulouse", 50),
    tarif_train("Lille", "Nantes", 50)
]
resultat_fonction = (ecart_type(ltrf))
print(f"L'écart type est de : {resultat_fonction} €")

print("\n*** Test 3 : Valeurs dispersées ***")
ltrf = [
    tarif_train("Paris", "Lyon", 10),
    tarif_train("Paris", "Marseille", 10),
    tarif_train("Paris", "Bordeaux", 10),
    tarif_train("Paris", "Toulouse", 10),
    tarif_train("Paris", "Nice", 95)
]
resultat_fonction = (ecart_type(ltrf))
print(f"L'écart type est de : {resultat_fonction} €")

print("\n*** Test 4 : moitié des valeurs ***")
ltrf = [
    tarif_train("Paris", "Lyon", 0),
    tarif_train("Paris", "Marseille", 0),
    tarif_train("Paris", "Bordeaux", 6),
    tarif_train("Paris", "Toulouse", 6)
]
resultat_fonction = (ecart_type(ltrf))
print(f"L'écart type est de : {resultat_fonction} €")

print("\n*** Test 5 : Grande liste lambda ***")
ltrf = [tarif_train("Crest", "Paris Gare de Lyon", 36),
    tarif_train("Les Aubrais", "Narbonne", 49),
    tarif_train("Caussade Tarn-et-Garonne", "Paris Gare de Lyon", 20),
    tarif_train("Saint-Christophe", "Paris Bercy", 21),
    tarif_train("Mérens-les-Vals", "Les Aubrais", 185),
    tarif_train("Cransac", "Paris Bercy", 59),
    tarif_train("Cransac", "Paris Gare de Lyon", 201),
    tarif_train("Tarascon-sur-Ariège", "Les Aubrais", 77),
    tarif_train("Capdenac", "Paris Bercy", 189),
    tarif_train("Capdenac", "Paris Gare de Lyon", 83),
    tarif_train("Figeac", "Paris Gare de Lyon", 89),
    tarif_train("Paris Austerlitz", "Rodez", 28),
    tarif_train("Paris Bercy", "Saint-Denis-près-Martel", 43),
    tarif_train("Carmaux", "Les Aubrais", 86),
    tarif_train("Paris Austerlitz", "Cahors", 50),
    tarif_train("Gramat", "Paris Austerlitz", 67),
    tarif_train("Saint-Christophe", "Les Aubrais", 39),
    tarif_train("Les Aubrais", "Viviez-Decazeville", 174),
    tarif_train("Assier", "Les Aubrais", 169),
    tarif_train("Laroquebrou", "Paris Austerlitz", 12)]
resultat_fonction = (ecart_type(ltrf))
print(f"L'écart type est de : {resultat_fonction} €")

        
