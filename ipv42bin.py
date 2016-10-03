#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def get(prompt='', allow_empty=False):
    try:
        r = input(prompt)
    except EOFError:
        print('')
        get(prompt)
    except KeyboardInterrupt:
        print('')
        exit()
    else:
        return r if r != '' or allow_empty else get(prompt)

usage = '''USAGE: {} ADDR
where ADDR is an IPv4 address (eg. 192.240.142.10)
'''

try:
    exe, arg = sys.argv
except ValueError:
    print(usage, file = sys.stderr)
    exit(1)

for i in arg.split('.'):
    arg.replace(i, bin(int(i))[2:])
print(arg)
