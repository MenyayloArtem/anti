import os, re
from os.path import isdir, isfile

def get_dir(path = ".", files = False, ext = None):
    if files:
        res = [f for f in os.listdir(path) if not os.path.isdir(os.path.join(path, f))]
        regexp = re.compile(f"{ext}$")
        res = list(filter(lambda f : re.search(regexp, f), res))
    else:
        res = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    return res