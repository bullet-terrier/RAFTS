# wipeold.py
# daily clear oldest script... do we really need this?

import os;
import shutil;
import find_file;

path = None;
pattern = None;

def killit(path_=path, pattern_=pattern):
    """
    """
    if pattern_ is None: pattern = "";
    y = find_file.find_least_recent_file(path_,pattern_)[0]
    if "wipeold.py" not in y: os.remove(y); # not equal to wouldn't have handled an absolute path to this file... would've been foolish.
    return;

if __name__=="__main__":
    path = input("Enter the search path to match: ") or path;
    pattern = input("Enter the search pattern to match: ") or pattern;
    killit(path,pattern);