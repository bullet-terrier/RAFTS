#
"""
TOday is gonna be one of those days apparently...

Looking at how to see if a directory has changed.
Might be a better way - but this ought to be adequate
if we're counting renaming as changed.
"""

import os
import hashlib

# section zero - general functions that all subsequent sections will use.
def hash_array(
    array_object:"Must be list or Tuple",
    hash_object:"Should be hashlib.x, default is sha256" = None,
    object_encoding:"Ascii,UTF-8,UTF-16" = None
    ):
    """
    Output will be directly to the caller via a return.
    returns the hexdigest for the array when cast into bytes.
    additional checks will be up to the caller.
    anything that is causing an issue will either raise an exception
    or be cast to a string.

    My (not so) secret goal is to be able to hash seemingly disparate types.
    """
    if type(array_object) not in [list]: raise ValueError("array_object must be a list type.")
    collector = b'';
    if hash_object is None: hash_object = hashlib.sha256;
    if object_encoding is None: object_encoding = 'ascii';
    for a in array_object:
        # handle types of a:
        if type(a) in [bytes]: collector+=a;
        if type(a) in [str]: collector+=bytes(a,object_encoding); # easy enough
        if type(a) in [int]: collector+=a;
        if type(a) in [float]:
            print("Warning: data loss may occur when converting floating point numerics to 'byte'")
            collector += bytes(int(a)); # we might deal with a loss of data on this one.
        
    
# section one - look at file names


# section two - look at access/creation times


# section three - look at file contents.
