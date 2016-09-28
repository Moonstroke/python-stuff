#!/usr/bin/python3
#coding: utf-8

from random import randrange

def en_string(list):
    s = ''
    for k in list:
        s += k
    return s

def get(prompt):
    try:
        r = input(prompt)
    except EOFError:
        print('')
        get(prompt)
    except KeyboardInterrupt:
        print('')
        exit()
    else:
        return r if r != '' else get(prompt)


class Grille(object):
    '''Instancie une grille de dimensions `hauteur` par `largeur`
'''
    
    def placer_mines(self, n_mines):
        for _ in range(n_mines):
            i = randrange(len(self.grille))
            self.grille[i] = '@'
    
    def en_grille(self, hauteur, largeur):
        self.grille = [self.grille[i:i + largeur] for i in range(0, len(self.grille), largeur)]
        if len(self.grille) != hauteur: raise ValueError('Incorrect hauteur')
    
    def __init__(self, hauteur, largeur, n_mines):
        self.grille = ['.'] * hauteur * largeur
        self.placer_mines(n_mines)
        self.en_grille(hauteur, largeur)
        self.fini = False
        self.victoire = False
    
    def __repr__(self):
        r = '+' + '-' * len(self.grille[0]) + '+\n'
        for l in self.grille:
            r += '|' + en_string(l) + '|\n'
        r += '+' + '-' * len(self.grille[-1]) + '+\n'
        return r
    
    def verifier_case(self, x, y):
        try: return x >= 0 and y >= 0 and self.grille[y][x] in '@P!'
        except IndexError: return False
    
    def mines_adjacentes(self, x, y):
        ww = self.verifier_case(x - 1, y)
        nw = self.verifier_case(x - 1, y - 1)
        nn = self.verifier_case(x, y - 1)
        ne = self.verifier_case(x + 1, y - 1)
        ee = self.verifier_case(x + 1, y)
        se = self.verifier_case(x + 1, y + 1)
        ss = self.verifier_case(x, y + 1)
        sw = self.verifier_case(x - 1, y + 1)
        return ww + nw + nn + ne + ee + se + ss + sw
    
    def ouvrir_cases(self, x, y):
        z = self.mines_adjacentes(x, y)
        if z == 0:
            try:
                self.grille[y][x] = ' '
                self.open_tiles(x - 1, y)
                self.open_tiles(x - 1, y - 1)
                self.open_tiles(x, y - 1)
                self.open_tiles(x + 1, y - 1)
                self.open_tiles(x + 1, y)
                self.open_tiles(x + 1, y + 1)
                self.open_tiles(x, y + 1)
                self.open_tiles(x - 1, y + 1)
            except: pass
        else:
            self.grille[y][x] = str(z)
    
    def cliquer(self, x, y):
        if self.grille[y][x] == '.':
            self.ouvrir_cases(x, y)
            self.victoire = not [l for l in self.grille if '@' in l]
        elif self.grille[y][x] == '@':
            self.grille[y][x] = '#'
            self.fini = True

    
    def marquer(self, x, y):
        '''Switch between '.', 'F' and '?' if tile is safe, or '@', 'P', '!' if tile is mined.
'''
        m = {'.': 'F', 'F': '?', '?': '.', '@': 'P', 'P': '!', '!': '@'}
        self.grille[y][x] = m[self.grille[y][x]]


h, w, n = map(int, (get('Hauteur de la grille: '), get('Largeur de la grille: '), get('Nombre de mines: ')))
grille = Grille(h, w, n)

while not grille.fini:
    print(repr(grille))
    a = ''
    while a not in ('c', 'm'):
        a = get('Action: [c]lic/[m]arque ')
    x, y = map(int, (get('X = '), get('Y = ')))
    if a == 'c':
        grille.cliquer(x, y)
    elif a == 'm':
        grille.marquer(x, y)
