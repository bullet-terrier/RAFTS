#!##PYTHONPATH##

"""
Benjamin Tiernan

2018-03-20

RAFTS is the Rapid Automatic File Transfer Solution
essentially will allow us to have scheduled cenralized EFT output.

There will be specific push directories that RAFTS will look for.
RAFTS can run on Linux and Windows interchangeably, though linux
is the preferred operating system.

please see the README.MD file for more information.

update 2018-03-20: Benjamin Tiernan: Updating to list the last runtime.
                   Will need to set up some thresholds between which it should
                   raise alarms if it hasn't run.
"""

import os;
import sys;
import platform;
import time;

# contains the definition for accessing directories in the dependency nodes.
# this is currently relative to the calling directory - need to set this up
# to allow it to be called from anywhere.
p2d_l = (os.curdir,os.sep,os.sep); # path two nodes down from local.
p1d_1 = (os.curdir,os.sep);

# gain access to localized dependencies.
sys.path.append("%s%sDependencies%scommon"%p2d_l);
sys.path.append("%s%sDependencies%smodules"%p2d_l);
sys.path.append("%s%sMappings"%p1d_1);

import log_function as lumberjack;
import rafts_ftp as creek;
import rafts_map as river;

##### ALIASES #####
log = lumberjack.log_output
stdlg = "%s%sLogs%sactivity_log.log"%(os.curdir,os.sep,os.sep);
errlg = "%s%sLogs%serror_log.log"%(os.curdir,os.sep,os.sep);
paddle = river.library;
banjo = creek.ftp_script;

# log generation confirmed.
#log("test standard log",stdlg)
#log("test error log",errlg)

# mapping utility - determine credentials and the specifics of the rafts_ftp call?

def main(arg):
    """
    attempting to use the river.
    """
    t = time.time();
    with open("%s%sDependencies%sdata%s.lastrun"%(p2d_1,os.sep),'w') as o: o.write(str(time.time()));
    try:
        log("attempting to send: %s"%(arg),stdlg)
        # don't forget that you have to expand the argument that you're passing.
        ret_code =banjo(**paddle[arg])
        log("Return data: %s\tTime Elapsed: %s"%(str(ret_code),time.time()-t),stdlg)
        if ret_code[1] not in [None,False]: 
            log("Encountered exception when sending %s; attempted with arguments %s;"%(arg,paddle[arg]),stdlg)
            log("Return code: %s"%(ret_code[0]),stdlg)
            log("elapsed time: %s"%(time.time()-t),stdlg)
            # forgot to bring this back
            raise Exception("Error encountered when sending file! %s. time Elapsed: %s"%(ret_code,time.time()-t))
        elif ret_code[0] in [None] and ret_code[1] in [None,False]: 
            log("successfully sent: %s: args: %s\t elapsed time: %s"%(arg,paddle[arg],time.time()-t))
        #log("Presumably sent without a hitch, time elapsed: %s"%(time.time()-t),stdlg)
        else:
            log("There might be an error, please check to make sure that the file was sent...");
    except Exception as EDNA:
        log("Exception encountered, see error log\t TIME ELAPSED: %s."%(time.time()-t),stdlg)
        log("Exception encountered: %s"%(str(EDNA)),errlg);
        log("TIME ELAPSED: %s"%(time.time()-5),errlg)
        sys.stderr.write("Exception has occurred!\nplease see: %s\n\nMESSAGE: %s\n\n"%(errlg,str(EDNA)))
        
def test_me():
    # for testing purposes:
    with open(stdlg,'r') as dt:
        x = dt.readline();
        while x not in [None,'']: 
            sys.stdout.write(x)
            x = dt.readline()
    sys.stdin.readline();    
    with open(errlg,'r') as dt:
        x = dt.readline();
        while x not in [None,'']: 
            sys.stdout.write(x)
            x = dt.readline()

if __name__=="__main__":
    # Adding in not 
    log("INITIALIZED RAFTS: %s"%(str(sys.argv)),stdlg);
    # need to determine what all will go into the mapping portion...
    sys.stdout.write("Welcome to RAFTS\r\n#UpACreek\r\n");
    creek.ftp_script_help();
    # exclude the current executable name
    for a in sys.argv[1:]:
        print(a)
        main(a);
else:
    log("RAFTS HAS BEEN IMPORTED...",stdlg);
    sys.stdout.write("Welcome to RAFTS\r\n#UpACreek\r\nIMPORTED!\r\n")