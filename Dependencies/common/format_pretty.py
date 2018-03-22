#!/usr/bin/python
"""

"""

import os
import shutil
import sys

def format_pretty(directory=None,contains = None):
    """
    make files within a directory match pattern defined below.
    """
    directory = directory or os.curdir;
    contains = contains or "";
    dir = [];
    for a in os.listdir(directory):
        if contains in a: dir.append(a)
    os.chdir(directory);
    for a in dir:
        b = a.replace('pretty_','');
        b = b.replace(' ','');
        b = b.replace('Rec','');
        shutil.move(a,b);
        
        
if __name__=="__main__":
    print("using none will be a wildcard.")
    contains = input("Please enter a pattern to match: ")
    for a in sys.argv:
        format_pretty(a,contains);
        