#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, getopt

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

x_py, *args = sys.argv
_help = '''Reads an CSV table and translates it into HTML format table.

Usage: {0} [OPTION] [CSV_FILE]

OPTION can be:
   -h | --help        displays this text and exits
   -c | --csv FILE    use file as input
   -o | --output FILE print result in FILE
   -H | --header      the first row is to be interpreted as heading row
   -s | --sep         separator to use (default is `,`)

The input file can be provided without the `-c`/`--csv` flag, but output file can not.
'''. format(x_py)

def translate(t, h, s):
    r = '<table>\n'
    for y in t.split('\n'):
        r += '<tr>\n'
        if h:
            _s, _e = '<th>', '</th>\n'
            h = False
        else:
            _s, _e = '<td>', '</td>\n'
        for x in y.split(s):
            r += _s + str(x) + _e
        r += '</tr>\n'
    return r + '</table>'

opts, args = getopt.gnu_getopt(args, 'hc:o:Hs:', ['help', 'csv=', 'output=', 'header', 'sep'])
_in = sys.stdin
out = sys.stdout
has_header = False
sep = ','
for a, o in opts:
    if a in ('-h', '--help'):
        print(_help)
        exit()
    elif a in ('-c', '--csv'):
        _in = open(o, mode='rt')
    elif a in ('-o', '--output'):
        out = open(o, mode='wt')
    elif a in ('-H', '--header'):
        has_header = True
    elif a in ('-s', '--sep'):
        sep = o
    else: raise ValueError('Unknown argument: ' + repr(a))

if _in == sys.stdin and len(args) == 1:
    _in = open(args[0])

table = _in.read()
print(repr(table))

print(translate(table, has_header, sep), file=out)

_in.close()
out.close()
