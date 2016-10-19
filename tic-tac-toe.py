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
    return r if r != '' or allow_empty else get(prompt)

def _repr(g):
    r = '+-+-+-+\n'
    for y in g:
        for x in y:
            r += '|' + x
        r += '|\n'
    r += '+-+-+-+\n'
    return r

def turn(g, x, y, k):
    if g[y][x] == ' ':
        g[y][x] = k
    else:
        raise Exception

def over(g):
    _x = any([g[0][x] == g[1][x] == g[2][x] for x in range(3) if g[0][x] != ' '])
    _y = any([y[0] == y[1] == y[2] for y in g if y[0] != ' '])
    _diag = (g[0][0] == g[1][1] == g[2][2] or g[0][2] == g[1][1] == g[2][0]) and g[1][1] != ' '
    return _y or _x or _diag

player = lambda ox: 'o' if ox else 'x'

grid = [[' ' for _ in range(3)] for _ in range(3)]
O_X = True #True <=> O, False <=> X
victory = False
nb_turns = 0
while not victory and nb_turns < 9:
    print('Turn no : ' + str(nb_turns) + '\n' +  _repr(grid) + '\n\nPlaying : ' + player(O_X).upper())
    try:
        x, y = get('Enter case coords: ')
        turn(grid, int(x), int(y), player(O_X))
    except Exception:
        print('Nope! Try again.')
        continue
    O_X = not O_X
    nb_turns += 1
    victory = over(grid)
if victory:
    print(_repr(grid), '\n\nVictory of ' + player(not O_X).upper() + ' !')
else:
    print('Blocked!')
