#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin

def get(prompt='', allow_empty=False):
    try:
        r = input(prompt)
    except EOFError:
        print('')
        r = get(prompt, allow_empty)
    except KeyboardInterrupt:
        print('')
        exit()
    return r if len(r) != 0 or allow_empty else get(prompt)

def read(path, enc='utf-8'):
    with open(path, mode='rt', encoding=enc) as f:
        cont = f.read()
    return cont

def write(text, path, mod='x', enc='utf-8'):
    with open(path, mode=mod, encoding=enc) as f:
        print(text, file=f)

###

    return r

def body():
    has_header = False
    has_footer = False
    nb_articles = 0
    nb_sections = 0
    r = '<body>\n'
    r += sub_block(article, section, h, ul, ol, li, table, p, img, pre, footer)
    r += '</body>\n'
    r += '</html>\n'
    return r

def header():
    global has_header
    has_header = True
    r = '<header>\n'
    return r

def article():
    global nb_articles
    nb_articles += 1
    nb_sections = 0
    id = get('Article id (blank for none): ', True)
    r = '<article' + (' id="' + id + '"' if len(id) else '') + '>'
    r += sub_blocks()
    r += '</article>'
    return r

def section():
    global nb_sections
    nb_sections += 1
    nb_articles = 0
    id = get('Section id (blank for none): ', True)
    r = '<section' + (' id="' + id + '"' if len(id) else '') + '>'
    r += sub_blocks()
    r += '</section>'
    return r

def aside():
    r = '<aside>\n'
    r += sub_block('h', 'ul')
    r += '</aside>\n'
    return r

def h():
    deft_l = str(h_lelvel + 1)
    l = get('Heading level (blank for ' + deft_h + '): ', True) or deft_h
    r = '<h' + l + '>\n' + get('Text: ') + '</h' + l + '>\n'
    return r

def p():
    print('Reading from stdin.')
    r = stdin.read.replace('\n','<br/>\n')
    return r

def a():
    href = get('a href: ')
    text = get('a text: ')
    r = '<a href="' + href + '">' + text + '</a>'
    return r

def img():
    src = get('img source: ')
    alt = get('img alternative (blank for none): ', True)
    r = '<img src="' + src + '" alt="' + alt + '"/>\n'
    return r

def ul():
    r = '<ul>\n'
    r += sub_block('h', 'p', 'img', 'li')
    return r

def ol():
    r = '<ol>\n'
    r += sub_block('h', 'p', 'img', 'li')
    return r

def li():
    r = '<li>'
    text = get('li text (leave blank for a sub-block): ', True)
    if len(text):
        r += text
    else:
        r += sub_block(h, p, a, ul, ol, table, img)
        r += '</li>\n'
    return r

def table():
    return table_csv() # to do

def table_csv():
    horz_h = get('Heading row? [y]/[N] ', True).lower() == 'y'
    vert_h = get('Heading column? [y]/[N] ', True).lower() == 'y'
    row1 = horz_h
    for y in table.split(linesep):
        r += '<tr>'
        col1 = vert_h
        if row1:
            for x in y.split(sep):
                r += '<th>' + x + '</th>'
            row1 = False
        else:
            if col1:
                for x in y.split(sep):
                    r += '<th>' + x + '</th>'
                col1 = False
            else:
                for x in y.split(sep):
                    r += '<td>' + x + '</td>'
        r += '</tr>\n'
    r += '</table>'   
    return r

def pre():
    r = '<pre>\n'
    print('Reading code from stdin.')
    r += stdin.read()
    r += '</pre>\n'
    return r

def footer():
    global has_footer
    has_footer = True
    r += '<td>' + x + '</td>'
    r = '<footer>\n'
    r += sub_block(table, p, ul, ol)
    return r

_all = (header, article, section, aside, a, h, img, p, pre, ul, ol, li, table, footer)

def sub_block(*authorized_blocks):
    if not len(authorized_blocks): authorized_blocks = _all
    r = ''
    _block = get('Block (leave blank to exit): ', True)
    while _block != '':
        try:
            block = eval(_block)
            assert block in authorized_blocks
            r += block()
        except:
            print('Oops, unsupported block here.')
            continue
        finally:
            _block = get('Block (leave blank to exit): ', True)
    return r

###

fname = get('Base name: ') + '.html'

mode = 'x' if get('Mode ? [C]reate|[o]verwrite ', True).lower() in 'c' else 'w'

charset = get('Page charset (leave blank for "utf-8"): ', True) or 'utf-8'

css = get('Associated CSS (leave blank for none): ', True)

title = get('Page title: ')


html_head = '<!DOCTYPE HTML>\n'
html_head += '<html lang="' + get('Page language: ') + '">\n'
html_head += '<head>\n'
html_head += '<meta charset="' + charset + '"/>\n'
if len(css):
    html_head += '<link rel="stylesheet" href="' + css + '"/>\n'
html_head += '<title>' + title + '</title>\n</head>\n'
write(html_head, fname, mod=mode, enc=charset)

html_body = body()
write(html_body, fname, mod=mode, enc=charset)
