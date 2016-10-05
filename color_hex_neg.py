#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv

usage = '''USAGE: {} [#]HEXVAL
Outputs the negative value of #HEXVAL
HEXVAL may begin with an '#', however one will always be output.
'''.format(argv[0])

try:
    exe, arg = argv
except:
    print(usage)
    exit(1)

if arg[0] == '#':
    arg = arg[1:]
m = (1 << 4 * len(arg)) - 1
print('#' + hex(m - int(arg, 16))[2:])
