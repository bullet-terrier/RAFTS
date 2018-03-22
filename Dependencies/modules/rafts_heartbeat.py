# !##PYTHONPATH##
"""
rafts.heartbeat

Monitor tool?

add mechanism for reporting 'x days since last error'

so far this is continuing to work, so I might need to expand it to allow more mapping
this will need to look at an array of data to write - possibly from a file,
that can be linked back to the functions that will execute.

I might have a dedicated mechanism for the main function.

Could set this to run either at reboot or at startup - which should function 
for the recovery.

looks like it is primarily the "main" functino that would need to change.
the check_run mechanism is working well.

heartbeat runs whether the user is logged in or not - which means that I'll
need to add in a condition for the main tool to report the PID of the currently
running mechanism and kill it should we start a new one.


Also need to see if the process slows down as the process continues. it looks
like there might be some minor fluctuation in the execution time based on which
sub-second time the counter goes off on.

Lastly, if it gets established as a system service, then I'll be capable of
controlling it through systemctl (linux only) but would reduce the type
support that the process would have on windows machines.

Removing the attachment as it isn't necessary. If someone wants that as
part of the report, then they can seek it out themselves.


*** NOTE !! ***

THIS VERSION OF "HEARTBEAT"
WILL BE DEPRECATED BY AN INDEPENDENT MODULE.

THIS IS A PROTOTYPE MODEL THAT MIGHT BE DIFFERENT
THAN ANY SUBSEQUENT MODELS.

NEW ADDITION FOR THE RAFTS_HEARTBEAT:
Adding in "LOCKFILE" to allow it to be persistently checked

It will be registered as a system service on the linux machine
and 

***         ***

Might try using queues for some other processes - don't need to implement that
for any currently in-use process.

"""

#
import sys;
import time;
import sched;
import os;
import math;

# success alert users:
default_alert = [
  #'kzearfoss.contractor@stins.com',
  'btiernan@stins.com'
]
# error alert users:
error_alert = [
  #'kzearfoss.contractor@stins.com',
  'btiernan@stins.com'
]

# This will need to be parameterized away into some
# configuration file. Additionally - I'm going to need
# some kind of handle on when the mechanism is running.
# Maybe set the file to "Nostart?" or attempt to restart 
# the service?

# path to the file that we're monitoring
check_path = "./.last_run";
# unused
check_paths = [];
# update with the path to the common tools that ship with the program.

common_path = "%sRAFTS%sDependencies%scommon"%(os.sep,os.sep,os.sep);
data_path = "%sRAFTS%sDependencies%sdata"%(os.sep,os.sep,os.sep);
lock_path = "%s%s./.rafts_heartbeat.lock"%(os.sep,data_path);

# modify this to change the delay between beats. (in seconds)
heartbeat = 360;
# 
# Try utilizing a localized common mechanism.
# sys.path.append("../common");
#
import mailit as mailman;
import log_function as lumberjack;

# bring in the kwargs parser;
from kwargs_konsolidator import *;
    

### ALIASES ###
log = lumberjack.log_output;

# I've got a cleaner version that I might merge with this one.
def check_run(**args):
    """
    arguments:
        file:[path to file]
        threshold:[number in seconds (rounded down) to allow]
    will return a tuple with the value, and whether or not to 
    raise an alarm (ie (49,true))
    """
    args_ = {
        "file":None,
        "value":0,
        "threshold":0,
        "message_data":0,
        "timer":0
    }
    # changing it back over to "args", not the recommended 
    # way to use reconcile, but is a decent way to implement it.
    # Because I'm a jerk, I'm making this version slightly less readable.
    args = reconcile(args_,args); 
    del args_;
    now,value = time.time(),0;
    #value = 0;
    raise_alert,message_data = False,None;
    #message_data = None;
    file_name,threshold = args['file'],float(args['threshold']);
    #threshold = float(args['threshold'])
    if not os.path.exists(file_name): 
        raise_alert =  True; 
        message_data = "It appears that the file %s does not exist. Checked at: %s"%(file_name,time.strftime("%Y-%m-%d %H:%M:%S"))
        log(message_data);
    tmr = None;
    with open(file_name,'r') as data:
        tmr = data.read();
    try:
        tmr = float(tmr)
        log("Time data found for %s"%(file_name));
    except Exception as Epsilon:
        raise_alert = True;
        tmr = 0;
        message_data = "The time component couldn't be isolated...."
        log("%s: time component could not be isolated. flagging alert to be raised.")
    # now to compare the numeric values:
    value = math.ceil(now-tmr);
    if value<threshold:
        message_data = "Last run within threshold amount: time was %s."%(str(value));
    else:
        message_data = "Last run was not within the threshold, flagging for alert. Time was %s"%(str(value))
        raise_alert = True;
    log(message_data);
    return(message_data,raise_alert);
    
# I'll be shipping a version 2 that takes a singular key for the alert list (derived from the mailing_list.py)
def main(arg,alert_list=None,this_thresh = 0,caller=None):
    """
    'modular' main - can replace this component as needed 
    to make upgrades.
    """
    #now = time.time()
    log("Initialized rafts_heartbeat for execution.");
    #with open("./.last_run",'w') as d: d.write(str(now));
    res = check_run(file = arg,threshold=this_thresh)
    if res[1] is True and alert_list is not None:
        mailman.send_mail("heartbeat@stins.com",alert_list,"[WARNING] Heartbeat update",res[0],"./activity_log.log","webmail.stins.com")
    else:
        mailman.send_mail("heartbeat@stins.com",default_alert,"[DATA] Heartbeat update",res[0],"./activity_log.log","webmail.stins.com")
    if caller is not None:
        print("Adding a new run entry... TIME IS: %s"%(time.strftime("%H:%M:%S")));
        next = time.time()+heartbeat;
        caller.enterabs(next,None,main,(arg,alert_list,this_thresh,caller));
        log("Scheduling next check for:%s"%(str(next)));
    return;

# Additional Methods "2018-03-22 Benjamin Tiernan";
# x_running() methods will be action control units.
def check_running():
    pass;
    
def exit_running():
    pass;
    
def start_running():
    pass;
    
    
# this is your entry point.
if __name__=="__main__":
    now = time.time();
    sys.stdout.write("Initialized the mechanism for rafts_heartbeat");
    zed = sched.scheduler(time.time,time.sleep);
    with open("./.last_run",'w') as d: d.write(str(now));
    #for a in check_paths: might modify this to just check all of the paths that it is given
    zed.enter(5,None,main,(check_path,error_alert,8,zed));
    log("Generated a heartbeat entity, should run until killed.");
    zed.run() # forgot to call the runner;
    
