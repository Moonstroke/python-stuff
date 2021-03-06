#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv, stdin

usage = '''USAGE: {} [ [#]HEXVAL...]
Outputs the negative value of #HEXVAL. Supports multiple arguments.
HEXVAL may begin with an '#', however one will always be output.
If called without argument, or argument is `-`, value is read from STDIN.
'''.format(argv[0])

try:
    exe, *args = argv
    if not len(args) or args[0] == '-':
        raise ValueError
    if args[0] in ('-h', '--help'):
        print(usage)
        exit(255)
except ValueError:
    args = stdin.read().split('\n')

i = 0
for arg in args:
    i += 1
    if not len(arg): continue
    m = (1 << 4 * len(arg)) - 1
    try:
        print('#' + hex(m - int(arg, 16))[2:])
    except:
        exit(i)
