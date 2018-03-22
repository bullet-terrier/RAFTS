#
"""
going to have to embed a copy of python - to move geics - I'm going to use
os.path.getmtime(x) for each file in the geics directory - at the time it
runs, it should be the most recent file. I'll add in a couple of checks
later to help me recognize that it is the geics file and not some other file.

Changes have been made to reflect some cases in which the "calculated realpath"
is inaccurate...
"""

import os;
import splash; # this isn't necessary, just fun.
from log_function import log_output as log
from tuple_comparisons import *;

def find_most_recent_file(search_path,pattern = None):
    """
    will attempt to find the most recently modified file in search_path,
    matching pattern "pattern". I'll probably adjust this to do a regex search
    later, but for now, it is only capable of a rudimentary contaiment search.
    
    Successfully locates the most updated file in a directory matching pattern -
    I'll add in a user interface of some sort for this, but for now it isn't necessary.
    """
    pattern = pattern or "";
    if type(search_path) != str: 
        log("TypeError occurred: [search_path] must be a string argument.","error_log.log");
        raise TypeError("[search_path] must be a string argument!");
    if type(pattern)!= str: 
        log("TypeError occurred: <pattern> must be a string argument.","error_log.log");
        raise TypeError("<pattern> must be a string argument!"); 
    if not os.path.isdir(search_path): raise Exception("input must be a path!");
    if not os.path.isabs(search_path):
        print("Warning: you may encounter errors if the path provided isn't local, or complete.\n\n%s"%(search_path))
    path_items = []
    for a in os.listdir(search_path):
        if os.path.isabs(search_path):
            a = search_path+os.sep+a;
        local_item = []
        #a #= os.path.realpath(a)
        print(a)
        if pattern not in a: continue
		# it appears that real path is causing an issue - I'll have to construct an absolute path.
        local_item.append(a); local_item.append(os.path.getmtime(a)); # tuple[1] will be the M time.
        log("Adding items to consider: %s"%(str(local_item))) # I could take these and store them... maybe in future development.
        path_items.append(tuple(local_item))
    most_recent = max_tup(path_items,1)
    return most_recent;
    
def find_least_recent_file(search_path,pattern = None):
    """
    will attempt to find the least recently modified file in search_path,
    matching pattern "pattern". I'll prabably adjust this to do a regex search
    later, but for now, only capable of a rudimentary containment search.
    """
    pattern = pattern or "";
    if type(search_path) != str:
        log("TypeError occurred: [search_path] must be a string argument.","error_log.log");
        raise TypeError("[search_path] must be a string argument!");
    if type(pattern) != str:
        log("TypeError occurred: <pattern> must be a string argument.","error_log.log");
        raise TypeError("<pattern> must be a string argument!");
    if not os.path.isdir(search_path): raise Exception("input must be a path!");
    if not os.path.isabs(search_path):
        print("Warning: you may encounter errors if the pat provided isn't local, or complete.\n\n%s"%(search_path))
    path_items = [];
    for a in os.listdir(search_path):
        if os.path.isabs(search_path):
            a = search_path+os.sep+a;
        local_item = []
        print(a);
        if pattern not in a: continue;
        local_item.append(a); local_item.append(os.path.getmtime(a));
        log("Adding items to consider: %s"%(str(local_item)));
        path_items.append(tuple(local_item))
    least_recent = min_tup(path_items,1);
    return least_recent;


