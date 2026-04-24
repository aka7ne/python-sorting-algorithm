#Kawthar Bouguima TP PROJET partie 1  09/03/2025
#Modification le 19/03/2025 ajout des fonction min max moyenne et écart type
#Modification le 25/03/2025 ajout de la fonction de filtrage "votre_type" (trf)
#Modification le 11/04/2025 ajout des fonction de tri, recherche dichotomiques et occurences
#Modification le 26/04/2025 modification des préconditions min max etc... liste non vide
"""
Ce fichier contient une fonction d'affichage de liste
ainsi qu'une tranformation en liste de liste et des fonction de calcul
ainsi qu'une fonction de filtrage
ainsi que des fonction de recherches dichotomique multiples et recherche d'occurence
"""
from KB_00_type import *
from outils_csv import *
from math import *


def affiche_liste_tarif( ltrf ) :
    """
    Rôle : Affiche la liste des informations des tarifs et gares des trains
    Données : ltrf (liste)
    Préconditions : ltrf doit être une liste d'objets de type tarif_train
    Résultat : Affichage des element de la liste

    """
    for i in range (len(ltrf)):
        affiche_tarif (ltrf[i])

def liste_de_listes_trf(liste_de_listes):
    """
    Rôle : Transforme liste de listes de chaine de charactere en liste de valeur de mon type "tarif_train"
    Données : liste de listes (liste)
    Préconditions: la liste doit avoir des sous-listes avec ces trois informations (origine, destination, prix)
    Résulat : liste d'objets de type "tarif_train"
    """
    ltrf = []
    for i in range(0, len(liste_de_listes), 1):
        liste = liste_de_listes[i]
        trf = tarif_train( liste[1], liste[3], int(liste[7]))
        ltrf.append(trf)
    return ltrf

def tarif_minimum (ltrf):
    """
    Rôle: retourne le minimum du tarif des train
    Données: ltrf liste d'objets tarif_train
    Préconditions: ltrf doit être une liste d'objets non vide de type tarif_train
    Résultat: float
    """
    tarif_min= ltrf[0].prix
    for i in range(1,len(ltrf),1):
        if tarif_min > ltrf[i].prix:
            tarif_min = ltrf[i].prix
    return tarif_min

def tarif_maximum (ltrf):
    """
    Rôle: retourne le maximum du tarif des trains
    Données: ltrf liste d'objets tarif_train
    Préconditions : ltrf doit être une liste d'objets non vide de type tarif_train
    résultat: float
    """
    tarif_max= ltrf[0].prix
    for i in range(1,len(ltrf),1):
        if tarif_max < ltrf[i].prix :
            tarif_max = ltrf[i].prix
    return tarif_max

def tarif_moyenne (ltrf):
    """
    Rôle: retourne la moyenne du tarif des trains
    Données: ltrf liste d'objets tarif_train
    Préconditions : ltrf doit être une liste d'objets non vide de type tarif_train
    résultat: float 
    """
    somme = 0
    for i in range(0, len(ltrf),1):
        somme += ltrf[i].prix
    moyenne = somme/len(ltrf)
    return moyenne

def ecart_type (ltrf):
    """
    Rôle: retourne l'écart type du tarif des trains
    Données : ltrf
    Préconditions : ltrf doit être une liste d'objets non vide de type tarif_train
    résultat: float
    """
    moyenne = tarif_moyenne(ltrf)
    somme = 0
    for i in range (len(ltrf)):
        somme += (ltrf[i].prix-moyenne)**2
    return sqrt(somme / len(ltrf))

def filtrage(ltrf, gare, origine_ou_destination):
    """
    Rôle : Filtre les tarifs des trains en fonction de la gare d'origine ou de destination
    Données : 
        ltrf : liste d'objets  de type tarif_train
        gare : chaîne de caractères représentant la gare à rechercher
        origine_ou_destination : chaîne de caractères pouvant être "origine" ou "destination"
    Préconditions : ltrf doit être une liste d'objets non vide de type tarif_train
               gare doit être une chaîne de caractères
               origine_ou_destination doit être soit "origine", soit "destination"
    Résultat : liste d'objets tarif_train
    """
    liste_filtree = []
    for i in range(len(ltrf)):
        tarif = ltrf[i]
        if origine_ou_destination == "origine" and tarif.gOrigine == gare:
            liste_filtree.append(tarif)
        elif origine_ou_destination == "destination" and tarif.gDestinataire == gare:
            liste_filtree.append(tarif)
    return liste_filtree



def liste_est_triee (ltrf):
    """
    Rôle : retourne True si la liste est triée selon les valeurs croissantes des prix, False sinon.
    Donnée : ltrf : liste d’objets de type tarif_train
    Préconditions : ltrf doit être une liste d'objets non vide ayant un attribut .prix
    Résultat : booléen (True ou False)
    """
    bool = True
    i=1
    while i<len(ltrf) and bool:
        if ltrf[i-1].prix>ltrf[i].prix:
            bool= False
        else: 
            i+=1
    return bool

def liste_tri_selection_minimum (ltrf):
    """
    Rôle : trie la liste ltrf selon les valeurs croissantes de prix, par la méthode de tri par sélection (du minimum dans ce cas).
    Donnée : ltrf : liste d’objets de type tarif_train
    Préconditions : ltrf doit être une liste d'objets non vide ayant un attribut .prix
    Résultat : liste d’objets de type tarif_train (triée selon le prix)
    """
    for i in range (0, len(ltrf),1):
        min_i=i 
        for j in range (i+1, len(ltrf),1):
            if ltrf[j].prix<ltrf[min_i].prix:
                min_i=j
        tmp= ltrf[i]
        ltrf[i]= ltrf[min_i]
        ltrf[min_i]= tmp
    return ltrf

def mediane(ltrf):
    """
    Rôle : détermine la médiane des prix dans la liste ltrf.
    Donnée : ltrf : liste d’objets de type tarif_train triée selon le prix
    Préconditions : ltrf doit être triée selon les prix et non vide
    Résultat : float
    """
    n= len(ltrf)
    if n%2 == 0:
        return (ltrf[n//2-1].prix + ltrf[n//2].prix)/2
    else:
        return ltrf[n//2].prix

def modalites(ltrf):
    """
    Rôle : retourne la liste des prix différents présents dans ltrf (appelés modalités).
    Donnée : ltrf : liste d’objets de type tarif_train triée selon le prix
    Préconditions : ltrf doit être triée selon les prix et non vide
    Résultat : liste de float ou int (les valeurs des prix sans doublons)
    """
    res= [ltrf[0].prix]
    for i in range(1, len(ltrf),1):
        if ltrf[i-1].prix < ltrf[i].prix:
            res.append(ltrf[i].prix)
    return res

def recherche_dichotomique (valeur, ltrf):
    """
    Rôle : effectue une recherche dichotomique d’un prix dans ltrf.
    Données : valeur : int (prix à chercher)
              ltrf : liste d’objets de type tarif_train triée selon le prix
    Préconditions : ltrf doit être triée selon les prix et non vide
    Résultat : entier (indice de la première occurrence trouvée ou -1 si absente)
"""
    g=0
    d= len(ltrf)-1
    res= -1
    while g<= d and (res==-1):
        m= (g+d)//2
        if ltrf[m].prix == valeur:
            res= m
        elif valeur < ltrf[m].prix:
            d= m-1
        else:
            g= m+1
    return res

def plus_petit_indice(valeur, ltrf):
    """
    Rôle : retourne l’indice de la première occurrence d’un prix donné dans ltrf.
    Données : valeur : int (prix à chercher)
              ltrf : liste d’objets de type tarif_train triée selon le prix
    Préconditions : ltrf doit être triée selon les prix et non vide
    Type du résultat : entier (indice de la première occurrence ou -1 si absente)
    """
    g = 0
    d = len(ltrf) - 1
    res = -1
    while g <= d:
        m = (g + d) // 2
        if ltrf[m].prix == valeur:
            res = m
            d = m - 1  
        elif valeur < ltrf[m].prix:
            d = m - 1
        else:
            g = m + 1
    return res
            
def plus_grand_indice (valeur, ltrf):
    """
    Rôle : retourne l’indice de la dernière occurrence d’un prix donné dans ltrf.
    Données : valeur : int (prix à chercher)
              ltrf : liste d’objets de type tarif_train triée selon le prix
    Préconditions : ltrf doit être triée selon les prix et non vide
    Résultat : entier (indice de la dernière occurrence ou -1 si absente)
    """
    g=0
    d= len(ltrf)-1
    res=-1
    while g <= d:
        m = (g+d) // 2
        if ltrf[m].prix == valeur:
            while m < len(ltrf)-1 and ltrf[m+1].prix == valeur:
                m += 1
            res= m
            g= m+1
        elif valeur < ltrf[m].prix:
            d= m-1
        else:
            g= m+1
    return res


def nombre_occurrence(valeur, ltrf):
    """
    Rôle : retourne le nombre d’occurrences d’un prix donné dans ltrf.
    Données : valeur : int (prix à chercher)
              ltrf : liste d’objets de type tarif_train triée selon le prix
    Préconditions : ltrf doit être triée selon les prix
    Résultat : entier (nombre d’occurrences, ou -1 si la valeur n’existe pas)
    """
    premier_indice = plus_petit_indice(valeur, ltrf)
    if premier_indice == -1:
        nb = -1
    else:
        dernier_indice = plus_grand_indice(valeur, ltrf)
        nb = dernier_indice - premier_indice + 1
    return nb
