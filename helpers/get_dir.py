import os, re
from os.path import isdir

def get_dir(path = ".", files = False, ext = None):
    folders = os.listdir(path)
    regex = re.compile(f'({ext})$')
    isfile = r'(\w+)\.(\w+)'

    folders = list(filter(lambda d: (re.search(isfile, d) and re.search(regex, d)) if files else not re.search(isfile,d), folders))
    return folders