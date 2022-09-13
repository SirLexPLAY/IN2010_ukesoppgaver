# Oppgave 2 fra uke 35
# Implementere binærsøk rekursivt

from random import randint

def binear_sook_rec(liste, tall, low, high):
    """
    Funksjonen sjekker rekursivt hvorvidt tallet forekommer i listen.
    Antar elementene i listen er sortert i stigende rekkefølge.
    Dersom tallet finnes, returneres indeksen til der den forekommer i listen.
    Hvis tallet ikke finnes i listen, returneres -1.
    """
    
    i = int((high+low)/2)
    
    if low > high:
        return -1

    if liste[i] == tall:
        return i
    elif liste[i] < tall:
        n_low = i+1
        out = binear_sook_rec(liste, tall, n_low, high)
    elif liste[i] > tall:
        n_high = i-1
        out = binear_sook_rec(liste, tall, low, n_high)

    return out
    
    


def generer_liste(list_size, num_size):
    liste = []

    for _ in range(list_size):
        liste.append(randint(1, num_size))

    return liste


onsket_tall = randint(0, 30)
list_size = 20

liste = generer_liste(list_size, 30)
liste.sort()
print(liste)

print(f"Ønsket tall: {onsket_tall}, er på plass {binear_sook_rec(liste, onsket_tall, 0, len(liste)-1)}")