#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv, stdin, stdout, stderr
from getopt import gnu_getopt
from os import linesep

def get(prompt='', allow_empty=False):
    try:
        r = input(prompt)
    except EOFError:
        print('')
        return get(prompt)
    except KeyboardInterrupt:
        print('')
        exit()
    else:
        return r if r != '' or allow_empty else get(prompt)

x_py, *optargs = argv

usage = '''Reads a CSV table and translates it into HTML format table.

Usage: {0} [OPTION...] [CSV_FILE]

OPTION can be any or several of the following:

\t-h | --help        displays this text and exits
\t-i | --input  FILE use file as input (none => stdin)
\t-o | --output FILE print result in FILE (none => stdout)
\t-H | --horz-h      the first row is a heading
\t-v | --vert-h      the first column is a heading
\t-s | --sep    SEP  separator to use (default is `,`)
\t-I | --id     ID   add the id ID to the <table> markup
'''. format(x_py)

opts, args = gnu_getopt(optargs, 'hi:o:Hvs:I', ['help', 'input=', 'output=', 'horz-h', 'vert-h', 'sep=', 'id'])
_in = stdin
out = stdout
horz_h = False
vert_h = False
sep = ','
id = ''

for a, o in opts:
    if a in ('-h', '--help'):
        print(usage)
        exit()
    elif a in ('-i', '--input'):
        _in = open(o, mode='rt')
    elif a in ('-o', '--output'):
        out = open(o, mode='wt')
    elif a in ('-H', '--horz-h'):
        horz_h = True
    elif a in ('-v', '--vert-h'):
        vert_h = True
    elif a in ('-s', '--sep'):
        sep = o
    elif a in ('-I', '--id'):
        id = o
    else: print('Invalid argument: ' + a, file=stderr); exit(1)

if _in == stdin and len(args) == 1:
     _in = args[0].open()

table = _in.read()

r = '<table' + ('id="' + id + '"' if id else '') + '>\n'
row1 = horz_h
for y in table.split(linesep):
    r += '<tr>'
    col1 = vert_h
    if row1:
        for x in y.split(sep):
            r += '<th>' + x + '</th>'
        row1 = False
    else:
        for x in y.split(sep):
            if col1:
                r += '<th>' + x + '</th>'
                col1 = False
            else:
                r += '<td>' + x + '</td>'
    r += '</tr>\n'
r += '</table>'   
print(r, file=out)
_in.close()
out.close()
