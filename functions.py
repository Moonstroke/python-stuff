#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''This script is not to be used as a script, it just provides some functions I use.
Enjoy it!
'''

def get(prompt='', allow_empty=False):
    '''Improved version of the input built-in.'''
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

def listr(l):
    '''Since there is no builtin method or function to turn a list of str into one str (join is not obvious), here is a short one.'''
    return str(l[0]) + listr(l[1:]) if len(l) else ''

