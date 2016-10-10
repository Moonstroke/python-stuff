#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random as r
import sys

help_fr = '''
Jeu du Mastermind en version terminal.
Au lancement du programme il est demandé d'entrer la longueur de la combinaison : Si la longueur entrée est 0, le programme termine.
\tPrivilégier des valeurs entre 3 et 5 pour une bonne expérience de jeu.
La combinaison consiste en une suite de couleurs choisies aléatoirement dans un ensemble précisé ultérieurement.

Il est ensuite demandé d'entrer une tentative.
Les couleurs sont représentées par un seul caractère, et sont : 
\t- Rouge : r
\t- Vert : v
\t- Bleu : b
\t- Jaune : j
\t- Cyan (bleu ciel) : c
\t- Violet : p
\t- Noir : n
\t- Blanc : w

\tSi la longueur en caractères est différente de la longueur de la combinaison, la tentative sera à retaper.
La tentative est ensuite affichée en caractères arobase ('@') en couleurs, suivie d'un indice.
L'indice consiste en des caractères croisillons ('#') blancs ou noirs.
\tUn croisillon blanc indique qu'une des couleurs de la tentative est présente dans la combinaison, mais pas à la bonne place.
\tUn croisillon noir indique qu'une des couleurs de la tentative est correcte et à la bonne place dans la combinaison.
\tPas de croisillon indique que la couleur n'est pas dans la combinaison.
\tAttention : la position des croisillons est aléatoire et ne correspond pas à chaque caractère de la tentative.
Il est ensuite demandé d'entrer une nouvelle tentative ; et ansi de suite jusqu'à ce que la tentative soit correcte.
\tSi le nombre de tentatives atteint 8, c'est échoué, et la combinaison est dévoilée.
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

def out(el, pre = '\033[1m', suf = '\033[0m'):
    print(pre, end='')
    for i in el:
        print(str(i), end = ' ')
    print(suf)

def attempt(prompt, l, colors):
    att = get(prompt)
    if len(tent) != l:
        print('Longueur incorrecte.')
        return attempt(prompt, l, colors)
    else:
        return list(colors[i] for i in att)

def check(att, combo):
    if att == combo:
        return True, []
    else:
        hint = []
        for i, e in enumerate(att):
            if combo[i] == e:
                hint.append('\033[30m#')
            elif e in combi:
                hint.append('\033[37m#')
        r.shuffle(hint)
        return False, hint

colors = {'n': '\033[30m@',
          'r': '\033[31m@',
          'v': '\033[32m@',
          'j': '\033[33m@',
          'b': '\033[34m@',
          'p': '\033[35m@',
          'c': '\033[36m@',
          'w': '\033[37m@'}

if len(sys.argv) < 1:
    if sys.argv[1] in '--help':
        print(help_fr)
        exit()

att, n, over = '', 0, False

print('To print the rules, hit `' + sys.argv[0] + ' --help` on the terminal.')
combo = r.sample(list(colors.values()), int(get('Combo size: ')))
print('Availables colors: ' + str(list(colors)))

while not over and n < 8:
    n += 1
    tent_prompt = 'Attempt no ' + str(n) + ': '
    att = attempt(att_prompt, len(combo), colors)
    out(att)
    over, hint = verifier(att, combo)
    out(hint)
else:
    if over:
        print('You won in ' + str(n) + ' attempt' + ('s' * (n > 1)) + '!')
    else:
        print('Game over!')
        out(combo)
