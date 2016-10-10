#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time, sys

def get(prompt, allow_empty=False):
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

def write(_f, text):
    with open(_f, mode='xt') as f:
        print(text, file=f)

### Functions

def head():
    lg = get('Page language: ')
    ks = get('Charset (default: utf-8): ', True) or 'utf-8'
    t = get('Title: ')
    css = get('Associated CSS (leave blank for none): ', True)
    css = ('\n<link rel="stylesheet" href="' + css + '"/>') if css else ''
    r = '''<!DOCTYPE HTML>
<html lang="{0}">
<head>
<meta charset="{1}"/>{3}
<title>{2}</title>
</head>
'''.format(lg, ks, t, css)
    return r, t

def page_header(deft):
    h1 = get('Page h1 (default: title from <head>): ', True)
    r = '''<body>
<header>
<h1 id="{1}">{0}</h1>
</header>
'''.format(h1 or deft, 'top')
    return r

def header(id):
    h2 = get('Block h2: ')
    r = '''<header>
<h2 id="{0}">{1}</h2>
</header>
'''.format(id, h2)
    return r

def article(n):
    t = get('Title of article ' + str(n) + ': ')
    y, m, d = map(str, time.gmtime()[0:3])
    id = y+'-'+m+'-'+d if get('Set article id by hand? [y/N]: ', True) in 'Nn' else get('Article id: ')
    r = '''<article id="{0}">
<header>
<h2><a href="#{0}" title="Link to the article" rel="bookmark">{1}</a></h2>
</header>'''.format(id, t)
    n_sec = 0
    sub_b = get('Sub block (blank to quit): ', True)
    while sub_b:
        if sub_b == 'section':
            n_sec += 1
        r += sub_blocks(sub_b, id, n_sec)
        sub_b = get('Sub block (blank to quit): ', True)
    r += '</article>\n'
    return r

def section(id_a, n):
    t = get('Title of section ' + str(n) + ': ')
    id = get('Section id (leave blank for default): ', True) or id_a + '-' + repr(n)
    r = '<section id="' + id + '">' if id else '<section>'
    r += get_sub_blocks(id, n, 0) + '''</section>
'''
    return r

def form():
    action, method = get('Action: '), get('Method: ')
    inputs = []
    has_submit = False
    _type = get('Input type: (leave blank to stop) ', True)
    while _type:
        if _type == 'submit':
            has_submit = True
        name, value = get('Input name: '), get('Input value: ')
        inputs.append((_type, name, value))
        _type = get('Input type: (leave blank to stop) ', True)
    if not has_submit:
        inputs.append(('submit', '', ''))
    r = '''<form action="{0}" method="{1}">
'''.format(action, method)
    for i in inputs:
        r += '''<input type="{0}" name="{1}" value="{2}"/>
'''.format(i[0], i[1], i[2])
    r += '</form>\n'
    return r

def pre():
    print('Reading code from standard input: ')
    code = sys.stdin.read()
    return '<pre>\n' + code + '\n' * (not code.endswith('\n')) + '</pre>\n'

def footer():
    r = '<footer>\n'
    
    return r + '</footer>\n'

def page_footer():
    return '''<footer>
<p><a href="#top" title="Go back to the top of page">Back to top</a></p>
</footer>
</body>
</html>
'''

#

def blocks(b, n, title = ''):
    _blocks = {'header': 'page_header(title)',
               'article': 'article(n)',
               'footer': 'page_footer()'
               }
    return eval(_blocks[b])

def sub_blocks(s_b, parent_id = None, s_n = 0):
    _blocks = {'header': 'header(parent_id)',
               'section': 'section(parent_id, parent_n, s_n)',
               'form': 'form()',
               'pre': 'pre()',
               'footer': 'footer()'
               }
    return eval(_blocks[s_b])

def get_sub_blocks(p_id, s_n):
    r = ''
    sub_b = get('Sub block (blank to quit): ', True)
    while sub_b:
        r += sub_blocks(sub_b, p_id, s_n)
    return r

###

f = get('Base name of the HTML file: ') + '.html'

head_html, def_title = head()

nb_articles = 0
has_header = False
has_footer = False

body_html = ''
block = get('Block: (leave blank to quit) ', True)
while block:
    if block == 'header': has_header = True
    elif block == 'article': nb_articles += 1
    elif block == 'footer': has_footer = True
    try:
        body_html += blocks(block, nb_articles)
    except KeyError:
        print('Oops, unsupported block type.')
    finally:
        block = get('Block: (leave blank to quit) ', True)
else:
    if not has_header: body_html = page_header(def_title) + body_html
    if not has_footer: body_html += page_footer()
    write(f, head_html + body_html)
    print('Written ' + f + '.')
