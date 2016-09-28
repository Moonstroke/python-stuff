#!/usr/bin/python3
#coding: utf-8

from random import randrange

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

def en_string(list):
    s = ''
    for k in list:
        s += k
    return s

class Grid(object):
    '''Instantiates a grid of dimensions `h` by `w`
'''
    
    def place_mines(self, n_mines):
        for _ in range(n_mines):
            i = randrange(len(self.grille))
            self.grid[i] = '@'
    
    def to_grid(self, hauteur, largeur):
        self.grille = [self.grille[i:i + largeur] for i in range(0, len(self.grille), largeur)]
        if len(self.grille) != hauteur: raise ValueError('Incorrect height')
    
    def __init__(self, h, w, n_mines):
        self.grille = ['.'] * h * w
        self.place_mines(n_mines)
        self.to_grid(hauteur, largeur)
        self.over = False
        self.vict = False
    
    def __repr__(self):
        r = '+' + '-' * len(self.grille[0]) + '+\n'
        for l in self.grille:
            r += '|' + to_string(l) + '|\n'
        r += '+' + '-' * len(self.grille[-1]) + '+\n'
        return r
    
    def check_case(self, x, y):
        try: return x >= 0 and y >= 0 and self.grid[y][x] in '@P!'
        except IndexError: return False
    
    def adjacent_mines(self, x, y):
        ww = self.check_tile(x - 1, y)
        nw = self.check_tile(x - 1, y - 1)
        nn = self.check_tile(x, y - 1)
        ne = self.check_tile(x + 1, y - 1)
        ee = self.check_tile(x + 1, y)
        se = self.check_tile(x + 1, y + 1)
        ss = self.check_tile(x, y + 1)
        sw = self.check_tile(x - 1, y + 1)
        return ww + nw + nn + ne + ee + se + ss + sw
    
    def open_tiles(self, x, y):
        z = self.adjacent_mines(x, y)
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
            self.grid[y][x] = str(z)
    
    def click(self, x, y):
        if self.grille[y][x] == '.':
            self.open_tiles(x, y)
            self.vict = not [l for l in self.grid if '@' in l]
        elif self.grid[y][x] == '@':
            self.grid[y][x] = '#'
            self.over = True

    
    def flag(self, x, y):
        '''Switch between '.', 'F' and '?' if tile is safe, or '@', 'P', '!' if tile is mined.
'''
        m = {'.': 'F', 'F': '?', '?': '.', '@': 'P', 'P': '!', '!': '@'}
        self.grid[y][x] = m[self.grid[y][x]]


h, w, n = map(int, (get('Height of the grid: '), get('Width: '), get('Number of mines: ')))
grid = Grid(h, w, n)

while not grid.fini:
    print(repr(grid))
    a = ''
    while a not in ('c', 'f'):
        a = get('Action: [c]lick/[f]lag ')
    x, y = map(int, (get('X = '), get('Y = ')))
    if a == 'c':
        grid.click(x, y)
    elif a == 'f':
        grid.flag(x, y)
