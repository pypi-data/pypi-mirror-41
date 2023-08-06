import pydecorator
from datetime import datetime
import urllib.request
from contextlib import closing
import re
import sys
import os


def getkey(d,key,default=None):
    """gets key from dict (d), if key does not exist, return default"""
    if key in d:
        return d[key]
    else:
        return default

@pydecorator.list
def extract(index,collection):
    for x in index:
        yield collection[x]

def is_iterable(a):
    if type(a)==str:
        return False
    try:
        iter(a)
        return True
    except TypeError:
        return False

# ============================================ Reduce ============================================ #

def iter_reduce(iterable,init=None):
    it = iter(iterable)
    try:
        v0 = next(it) if init is None else init
    except StopIteration:
        return
    for v1 in it:
        yield v0,v1
        v0 = v1

def reduce(fn,iterable,init=None):
    it = iter(iterable)
    try:
        value = next(it) if init is None else init
    except StopIteration:
        return None
    for e in it:
        value = fn(value,e)
    return value

# ============================================ time ============================================ #

def timestamp(ts):
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# TODO - timezones

# ============================================ urls ============================================ #


def is_url(path):
    return re.match(r'https?:\/\/',path)

def split_url(url):
    prefix = re.match(r'https?:\/\/',url)
    pieces = url[prefix.end(0):].split('/')
    domain = prefix.group(0)+pieces[0]
    return (domain,)+tuple(pieces[1:])


# ============================================ files ============================================ #

def read_file(file):
    if is_url(file):
        # Download File
        with closing(urllib.request.urlopen(file)) as response:
            return response.read().decode('utf-8')
        return
    with open(file,'r') as f:
        return f.read()

# ============================================ strings ============================================ #

def str_col(items,align='>'):
    # (> : right) (< : left) (^ : center)
    s = [str(i) for i in items]
    mx = max(len(x) for x in s)
    a = '{:%s%i}'%(align,mx)
    return [a.format(x) for x in s]

# ============================================ cli ============================================ #

# :---------:------:------:------------:----------:
# | Color   | Text |  BG  | BrightText | BrightBG |
# :---------:------:------:------------:----------:
# | Black   |  30  |  40  |    30;1    |   40;1   |
# | Red     |  31  |  41  |    31;1    |   41;1   |
# | Green   |  32  |  42  |    32;1    |   42;1   |
# | Yellow  |  33  |  43  |    33;1    |   43;1   |
# | Blue    |  34  |  44  |    34;1    |   44;1   |
# | Magenta |  35  |  45  |    35;1    |   45;1   |
# | Cyan    |  36  |  46  |    36;1    |   46;1   |
# | White   |  37  |  47  |    37;1    |   47;1   |
# :---------:------:------:------------:----------:

def cli_color(text,*colors):
    return "{}{}\x1b[0m".format("".join("\x1b[{}m".format(c) for c in colors),text)

def cli_warning(message):
    print("\x1b[31mWarning: {}\x1b[0m".format(message),file=sys.stderr)
