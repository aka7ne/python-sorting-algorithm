#Kawthar Bouguima fichier test n°11 calcul de médiane su liste pair et impaire
from KB_02_listes_type import *

print("\n*** Test 1: Liste paire ***")
ltrf=[tarif_train("Paris Austerlitz", "Rodez", 28),
    tarif_train("Tarascon-sur-Ariège", "Les Aubrais", 77),
    tarif_train("Capdenac", "Paris Gare de Lyon", 83),
    tarif_train("Figeac", "Paris Gare de Lyon", 89),
    tarif_train("Capdenac", "Paris Bercy", 189),
    tarif_train("Cransac", "Paris Gare de Lyon", 201)]
print(f"La médiane est de :", mediane(ltrf))


print("\n*** Test 2: Liste impaire ***")
ltrf= [ tarif_train("Bordeaux", "Toulouse", 36),
        tarif_train("Nice", "Lille", 45),
        tarif_train("Lyon", "Marseille", 55),
        tarif_train("Tarascon-sur-Ariège", "Les Aubrais", 77),
        tarif_train("Figeac", "Paris Gare de Lyon", 89)]
print(f"La médiane est de :", mediane(ltrf))

print("\n*** Test 3: Liste une seule valeur***")
ltrf = [tarif_train("Lyon", "Marseille", 90)]
print(f"La médiane est de :", mediane(ltrf))
