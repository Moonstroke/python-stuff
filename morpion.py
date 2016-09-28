#!/usr/bin/python3

def get(prompt):
    try:
       return input(prompt)
    except EOFError:
        print('')
        get(prompt)
    except KeyboardInterrupt:
        print('')
        exit()
    
def _repr(g):
    r = '+-+-+-+\n'
    for y in g:
        for x in y:
            r += '|' + x
        r += '|\n'
    r += '+-+-+-+\n'
    return r

def tour(g, x, y, k):
    if g[y][x] == ' ':
        g[y][x] = k
    else:
        raise Exception

def fini(g):
    _x = any([g[0][x] == g[1][x] == g[2][x] for x in range(3) if g[0][x] != ' '])
    _y = any([y[0] == y[1] == y[2] for y in g if y[0] != ' '])
    _diag = (g[0][0] == g[1][1] == g[2][2] or g[0][2] == g[1][1] == g[2][0]) and g[1][1] != ' '
    return _y or _x or _diag

joueur = lambda ox: 'o' if ox else 'x'

grille = [[' ' for _ in range(3)] for _ in range(3)]
O_X = True #True <=> O, False <=> X
victoire = False
nb_tours = 1
while not victoire and nb_tours < 10:
    print(u'Tour n° : ' + str(nb_tours) + '\n' +  _repr(grille) + '\n\nC\'est au tour de : ' + joueur(O_X).upper())
    try:
        tour(grille, int(get('x = ')), int(get('y = ')), joueur(O_X))
    except Exception:
        print('Non ! Recommence.')
        continue
    O_X = not O_X
    nb_tours += 1
    victoire = fini(grille)
if victoire:
    print(_repr(grille), '\n\nVictoire de ' + joueur(not O_X).upper() + ' !')
else:
    print('Bloqués !')
