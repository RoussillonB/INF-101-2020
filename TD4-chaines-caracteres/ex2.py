def pyramide_1():
    lettre = 'a' # Variable contenant la lettre courante à afficher
    i = 1
    while i <= 7:
        j = 1
        while j <= i:
            print(lettre, end='')
            if('a' <= lettre < 'z'):
                # La construction suivante est a maitriser
                lettre = chr(ord(lettre) + 1) # Si la lettre était une lettre de l'alphabet autre que z, il reste des lettres à parcourir
            else:
                lettre = '-' # Sinon on à déjà affiché toutes les lettres et il nous reste les -
            j += 1
        print() # Retour à la ligne
        i += 1
    # Pas de return, on ne fait qu'un affichage


def pyramide_2():
    count = 0 # Autre méthode: compteur qui détermine sur quelle lettre on est. 0 correspond à a.
    i = 1
    while i <= 7:
        j = 1
        # Sur chaque ligne, on à 7 - i espaces
        while j <= 7 - i:
            print(' ', end='')
            j += 1
        while j <= 7:
            if(count < 26):
                # La construction suivante est à maitriser
                print(chr(ord('a') + count), end='')
                count += 1
            else:
                print('-', end='')
            j += 1
        print() # Retour à la ligne
        i += 1


# Programme principal
pyramide_1()
pyramide_2()
