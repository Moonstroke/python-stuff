#!/usr/bin/python3
#coding: utf-8

import random as r
import sys

aide = '''
Jeu du Mastermind en version terminal.
Au lancement du programme il est demandé d'entrer la longueur de la combinaison : Si la longueur entrée est 0, le programme termine.
   Privilégier des valeurs entre 3 et 5 pour une bonne expérience de jeu.
La combinaison consiste en une suite de couleurs choisies aléatoirement dans un ensemble précisé ultérieurement.

Il est ensuite demandé d'entrer une tentative.
Les couleurs sont représentées par un seul caractère, et sont : 
 - Rouge : r
 - Vert : v
 - Bleu : b
 - Jaune : j
 - Cyan (bleu ciel) : c
 - Violet : p
 - Noir : n
 - Blanc : w

   Si la longueur en caractères est différente de la longueur de la combinaison, la tentative sera à retaper.
La tentative est ensuite affichée en caractères arobase ('@') en couleurs, suivie d'un indice.
L'indice consiste en des caractères croisillons ('#') blancs ou noirs.
   Un croisillon blanc indique qu'une des couleurs de la tentative est présente dans la combinaison, mais pas à la bonne place.
   Un croisillon noir indique qu'une des couleurs de la tentative est correcte et à la bonne place dans la combinaison.
   Pas de croisillon indique que la couleur n'est pas dans la combinaison.
   Attention : la position des croisillons est aléatoire et ne correspond pas à chaque caractère de la tentative.
Il est ensuite demandé d'entrer une nouvelle tentative ; et ansi de suite jusqu'à ce que la tentative soit correcte.
   Si le nombre de tentatives atteint 8, c'est échoué, et la combinaison est dévoilée.
'''
def get(prompt):
    try:
        i = input(prompt)
    except EOFError:
        print('')
        return get(prompt)
    except KeyboardInterrupt:
        print('')
        exit()
    else:
        return i if len(i) else get(prompt)

def out(el, pref = '\033[1m', suff = '\033[0m'):
    print(pref, end='')
    for i in el:
        print(str(i), end = ' ')
    print(suff)

def tentative(prompt, l, couleurs):
    tent = get(prompt)
    if len(tent) != l:
        print('Longueur incorrecte.')
        return tentative(prompt, l, couleurs)
    else:
        return list(couleurs[i] for i in tent)

def verifier(tent, combi):
    if tent == combi:
        return True, []
    else:
        indice = []
        for i, e in enumerate(tent):
            if combi[i] == e:
                indice.append('\033[30m#')
            elif e in combi:
                indice.append('\033[37m#')
        r.shuffle(indice)
        return False, indice

couleurs = {'n': '\033[30m@',
            'r': '\033[31m@',
            'v': '\033[32m@',
            'j': '\033[33m@',
            'b': '\033[34m@',
            'p': '\033[35m@',
            'c': '\033[36m@',
            'w': '\033[37m@'}

if len(sys.argv) < 1:
    if sys.argv[1] in '--help':
        print(aide)
        exit()

tent, n, fini = '', 0, False

print('Pour afficher les règles, tapez `' + sys.argv[0] + ' --help` dans le terminal.')
combi = r.sample(list(couleurs.values()), int(get('Taille de la combinaison = ')))
print('Couleurs disponibles : ' + str(list(couleurs)))

while not fini and n < 8:
    n += 1
    tent_prompt = 'Tentative n° ' + str(n) + ' : '
    tent = tentative(tent_prompt, len(combi), couleurs)
    out(tent)
    fini, indice = verifier(tent, combi)
    out(indice)
else:
    if fini:
        print('Gagné en ' + str(n) + ' coup' + ('s' * (n > 1)) + ' !')
    else:
        print('Perdu !')
        out(combi)
