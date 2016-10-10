#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def get(prompt='', allow_empty=False):
    try:
        r = input(prompt)
    except EOFError:
        print('')
        r = get(prompt)
    except KeyboardInterrupt:
        print('')
        exit()
    else:
        return r if r != '' or allow_empty else get(prompt)

def get_file(path):
    if path:
        with open(path, mode='rt') as f:
            r = f.read()
    else:
        r = sys.stdin.read()
    return r

def dbg(*l):
    print('\033[35m')
    for s in l:
        print(repr(s), end=' ')
    print('\033[0m')

###

def out(n):
    if n <= 32:
        n += 9216
    elif n == 127:
        n = 9249
    print(chr(n), end=' ')

def get_loops(p):
    s, e = 0, len(p)
    l = []
    while 0 <= s < e:
        s, e = p.find('[', s, e), p.find(']', s, e)
        l.append((s, e))
    return l[0:-1]
        
        
def test(val, loop):
    return not val, loop[not val]

def command(k, i, a):
    res = None
    try:
        if k == '<':
            i = i - 1 if i > 0 else len(a)
        elif k == '>':
            if i == len(a): a.append(0)
            i += 1
        elif k == '+':
            a[i] += 1
        elif k == '-':
            assert a[i] > 0
            a[i] -= 1
        elif k == ',':
            a[i] = ord(get('', True) or '\0')
        elif k == '.':
            out(a[i])
        elif k == '[':
            res = bool(a[i])
        elif k == ']':
            res = bool(a[i])
    except AssertionError:
        pass
    except IndexError:
        return command(k, i, a + [0])
    except TypeError:
        print('Error: Enter 1 char input')
        return command(k, i, a)
    return res, i, a

try:
    interpreter, path = sys.argv
except ValueError:
    path = ''
prog = get_file(path)
array = [0]
index = 0
loops = get_loops(prog)

char_num = 0
while char_num < len(prog):
    res, index, array = command(prog[char_num], index, array)
    #dbg(prog[char_num], index, array)
    if isinstance(res, bool):
        do_pop, char_num = test(res, loops[-1])
        if do_pop: loops.pop()
    char_num += 1
print()
