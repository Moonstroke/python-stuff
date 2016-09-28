#!/usr/bin/python3
# -*- coding: utf-8 -*-

def get(prompt, allow_empty=False):
    try:
        r = input(prompt)
    except EOFError:
        print('')
        return get(prompt)
    except KeyboardInterrupt:
        print('')
        exit()
    else: return r if r != '' or allow_empty else get(prompt)

def afficher_grille(grille):
    r = '  ABCDEFGHIJ'
    for i, y in enumerate(grille):
        r += '\n' + ' ' * (i + 1 < 10) + str(i + 1)
        for x in y:
            r += x
    print(r)

def placer_navire(g, l, ax, x, y):
    if l:
        if g[y][x] == '.':
            if ax[0]:
                placer_navire(g, l - 1, ax, x + 1, y)
            elif ax[1]:
                placer_navire(g, l - 1, ax, x, y + 1)
            g[y][x] = '@'
            
    #for j in range(y, y + (ax[1] * l or 1)):
    #    for i in range(x, x + (ax[0] * l or 1)):
    #        grille[j][i] = '@'

grille = [['.' for _ in range(10)] for _ in range(10)]

liste_bateaux = [2, 3, 3, 4, 5]

while liste_bateaux:
    afficher_grille(grille)
    print(liste_bateaux)
    b = int(get('Choisissez un bateau à placer : '))
    _axe = get('Quel axe ? [h]orizontal/[v]ertical ')
    if _axe in ('H', 'h'):
        axe = [1, 0]
    elif _axe in ('V', 'v'):
        axe = [0, 1]
    c = get('Case ? (exemple: H7) ')
    try:
        placer_navire(grille, b, axe, 'ABCDEFGHIJ'.find(c[0].upper()), int(c[1:]) - 1)
    except ValueError:
        continue
    liste_bateaux.remove(b)
afficher_grille(grille)
