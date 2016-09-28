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

def print_grid(grid):
    r = '  ABCDEFGHIJ'
    for i, y in enumerate(grid):
        r += '\n' + ' ' * (i + 1 < 10) + str(i + 1)
        for x in y:
            r += x
    print(r)

def place_ship(g, l, ax, x, y):
    if l:
        if g[y][x] == '.':
            if ax[0]:
                place_ship(g, l - 1, ax, x + 1, y)
            elif ax[1]:
                place_ship(g, l - 1, ax, x, y + 1)
            g[y][x] = '@'
            
    #for j in range(y, y + (ax[1] * l or 1)):
    #    for i in range(x, x + (ax[0] * l or 1)):
    #        grid[j][i] = '@'

grid = [['.' for _ in range(10)] for _ in range(10)]

list_ships = [2, 3, 3, 4, 5]

while list_ships:
    print_grid(grid)
    print(list_ships)
    sh = int(get('Choose a ship: '))
    _axis = get('Which axis ? [h]orizontal/[v]ertical ')
    if _axis in ('H', 'h'):
        axis = [1, 0]
    elif _axis in ('V', 'v'):
        axis = [0, 1]
    c = get('Tile ? (example: H7) ')
    try:
        place_ship(grid, sh, axis, 'ABCDEFGHIJ'.find(c[0].upper()), int(c[1:]) - 1)
    except ValueError:
        continue
    list_ships.remove(b)
print_grid(grid)
