#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv, stdin
from os import linesep

usage = '''USAGE: {} [IP_ADRESS...]
Outputs the binary representation of every IP_ADRESS
IP_ADRESS must be IPv4 format (e.g. `192.168.44.0`)
and will be ouput as bytes (e.g. `11000000.10101000.00101100.00000000`) of length always 8 bits.
If called without argument, or argument is `-`, value is read from STDIN.
On error exits with code the number of the failing value.
'''.format(argv[0])

try:
    exe, *args = argv
    if not len(args) or args[0] == '-':
        raise ValueError
    if args[0] in ('-h', '--help'):
        print(usage)
        exit(255)
except ValueError:
    args = stdin.read().split(linesep)

i = 0
for arg in args:
    i += 1
    if not len(arg): continue
    m = (1 << 4 * len(arg)) - 1
    try:
        r = ''
        for i in arg.split('.'):
            b = bin(int(i))[2:]
            b = '0' * (8 - len(b)) + b
            r += b + '.'
            print(r[:-1])
    except:
        exit(i)


