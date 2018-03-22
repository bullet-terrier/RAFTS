#!./Dependencies/python-3.6.4-emved-amd64/python.exe
"""
Cleanup .py
"""


# rough script to move all text files to the text graveyard.
extensions = [
    ".txt",
    ".scp",
    ".log",
    #".bat"
    
]
import datetime
tag = datetime.datetime.today().strftime
import os;
from shutil import move;

if not os.path.exists("./txt_graveyard"):
    os.makedirs("./txt_graveyard");

if os.path.exists("./txt_graveyard"):
    for a in os.listdir():
        for b in extensions:
            if b in a.lower(): 
                move(a,'./txt_graveyard/%s'%(tag("%Y%m%d_")+a))
                print("Moved: %s"%(tag("%Y%m%d_")+a))
		