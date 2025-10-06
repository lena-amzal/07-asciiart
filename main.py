#### Imports et définition des variables globales
# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    '''fonction itérative'''
    liste_tuples=[]
    nb_occurences=1
    carac_ref=s[0]
    for c in s[1:]:
        if c==carac_ref:
            nb_occurences+=1
        else:
            liste_tuples.append((carac_ref,nb_occurences))
            nb_occurences=1
            carac_ref=c
    liste_tuples.append((carac_ref,nb_occurences))
    return liste_tuples


def artcode_r(s):
    '''fonction récursive'''
    # cas de base
    if not s:
        return []
    # recherche nombre de caractères identiques au premier
    liste_tuple=[]
    i=1
    while i<len(s) and s[i]==s[0]:
        i+=1
    liste_tuple.append((s[0],i))
    # appel récursif
    r=liste_tuple+ artcode_r(s[i:])
    return r

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
