# Oppgave 1 fra uke 35
# Implementere binærsøk

from random import randint


def binear_sook(liste, tall):
    """
    Funksjonen sjekker hvorvidt tallet forekommer i listen.
    Antar elementene i listen er sortert i stigende rekkefølge.
    Dersom tallet finnes, returneres indeksen til der den forekommer i listen.
    Hvis tallet ikke finnes i listen, returneres -1.
    """

    low = 0
    high = len(liste)-1

    i = 0
    while low <= high:
        i = int((high+low)/2)

        if liste[i] < tall:
            low = i+1
        elif liste[i] > tall:
            high = i-1
        else:
            return i
    
    return -1


def generer_liste(list_size, num_size):
    liste = []

    for _ in range(list_size):
        liste.append(randint(1, num_size))

    return liste


onsket_tall = randint(0, 300)
list_size = 200

liste = generer_liste(list_size, 300)
liste.sort()
print(liste)

print(f"Ønsket tall: {onsket_tall}, er på plass {binear_sook(liste, onsket_tall)}")