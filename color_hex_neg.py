#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv, stdin

usage = '''USAGE: {} [ [#]HEXVAL]
Outputs the negative value of #HEXVAL
HEXVAL may begin with an '#', however one will always be output.
If called without argument, or argument is `-`, value is read from STDIN.
'''.format(argv[0])

try:
    exe, args = argv
except:
    args = stdin.read()
for arg in args.split('\n'):
    if len(arg) == 0:
        continue
    try:
        if arg[0] == '#':
            arg = arg[1:]
        m = (1 << 4 * len(arg)) - 1
        print('#' + hex(m - int(arg, 16))[2:])
    except:
        print(usage)
        exit(1)
