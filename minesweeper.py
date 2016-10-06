#!/usr/bin/python3
#coding: utf-8

from random import randrange

def get(prompt, allow_empty=False):
    try:
        r = input(prompt)
    except EOFError:
        print('')
        get(prompt)
    except KeyboardInterrupt:
        print('')
        exit()
    else:
        return r if r != '' or allow_empty else get(prompt, allow_empty)

def listr(l):
    r = l[0]
    for i in  l[1:]:
        r += i
    return r

class Grid(object):
    '''Instantiates a grid of dimensions `h` by `w`
'''
    
    _adj = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)] 
    def _mine(self, grid, n, h, w):
        placed = 0
        while placed < n:
            i = randrange(w)
            j = randrange(h)
            if grid[j][i] != -1:
                grid[j][i] = -1
                for d in self._adj:
                    _i = i + d[0]
                    _j = j + d[1]
                    try:
                        grid[_j][_i] += 1
                    except: continue
                placed += 1
            else:
                continue
        return grid
    
    def __init__(self, h, w, n):
        self.grid = self._mine([[0] * w] * h, n, h, w)
        self.surf = [['#'] * w] *h
        self.n_mines = n
        self.flags = []
        self.won = None
    
    def __repr__(self):
        r = '+' + '-' * len(self.surf[0]) + '+\n'
        for l in self.surf:
            r += '|' + listr(l) + '|\n'
        r += '+' + '-' * len(self.surf[-1]) + '+\n'
        return r
    
    def _kaboom(self, x, y):
        self.won = False
        self.surf[y][x] = '\033[31m@\033[0m'
        for _x, _y in self.flags:
            if self.grid[_y][_x] == -1:
                if self.surf[_y][_x] == 'F':
                    self.surf[_y][_x] = '\033[32mF\033[0m'
                else:
                    self.surf[_y][_x] = '@'
            else:
                if self.surf[_y][_x] == 'F':
                    self.surf[_y][_x] = '\033[33mF\033[0m'
    
    def open(self, x, y, is_played):
        z = self.grid[y][x]
        if z == 0:
            self.surf[y][x] = '.'
            for d in self._adj:
                _x = x + d[0]
                _y = y + d[1]
                if self.surf[_y][_x] == '#':
                    self.open(x, y, False)
        elif z == -1:
            if is_played:
                self._kaboom(x, y)
        else:
            self.surf[y][x] = str(z)
    
    def flag(self, x, y):
        if self.surf[y][x] == '#':
            self.flags.append((x, y))
            self.surf[y][x] == 'F'
        else:
            self.flags.remove((x, y))
            if self.surf[y][x] == 'F':
                self.surf[y][x] = '?'
            elif self.surf[y][x] == '?':
                self.surf[y][x] = '#'
            else:
                raise ValueError('What the hell!?')
            
    def check(self):
        if sum(int(self.grid[y][x] == -1) for x, y in self.flags) == self.n_mines:
            self.won = True
        

height, width, nb_mines = map(int, (get('Height of grid: '), get('Width of grid: '), get('Number of mines: ')))
grid = Grid(height, width, nb_mines)

while grid.won is None:
    print(repr(grid))
    a = ''
    while a not in ('o', 'f'):
        a = get('Action: [o]pen/[f]lag ').lower()
    x, y = map(int, (get('X = '), get('Y = ')))
    if a == 'o':
        if (x, y) in grid.flags:
            continue
        else:
            grid.open(x, y, True)
    elif a == 'f':
        grid.flag(x, y)
    grid.check()
print('\nYou {}!\n\n'.format('win' if self.over else 'lose'), repr(grid))
