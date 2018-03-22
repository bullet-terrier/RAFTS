#
"""
Setting up this script to functionally convert line endins
(need unix-style for published stuff.)

Will only work on files that can be completely opened within memory.
"""

import sys;
import os;

def strip_cr(file_path=None):
    """
    convert the line endings for a path, directories will attempt to traverse.
    I need to make sure that everything that is being committed will be able to strip the linefeed.
    """
    pass
    # 
    if os.isdir(file_path):
        for a in os.listdir():
            if os.path.isfile(a):
                buffer = None
                with open(a,'r') as data:
                    buffer = data.readlines();
                for b in buffer:
                    buffer[buffer.index(b)] = b.replace("\r","");
                with open(a,'w') as data:
                    data.write(buffer);
    return;