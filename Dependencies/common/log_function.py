#
"""
Time to build a better log module...
editing this to work with python 2.7

removing all decroators from the variable declarations.
"""
import datetime;
import os;

'@log'
#def log_output(contents:"string representation of information to write to log", logname :"path to the log file to write to. default is ./activity_log.log\n"= "activity_log.log"):
def log_output(contents,logname="activity_log.log"):
    """
    consistently write the files output to a log.
    """
    #__decorator__+=log
    n = datetime.datetime.now # get the time the value appears
    with open(logname,'a') as log:
        if type(contents) == list:
            for a in contents:
                log.write("%s\t%s"%(n().strftime("%Y-%m-%d %H:%M"),str(a)));
                if "\n" not in a:
                    log.write("\n");
        else:
            log.write("%s\t%s"%(n().strftime("%Y-%m-%d %H:%M"),str(contents)))
            if "\n" not in contents:
                log.write("\n");

log = log_output; # this might as well be used. I'm struggling to get the decorators to wrok.

class lumberjack:
    """
    class to contain all of the logging utilities.
    I'll have a couple of quick reference functions
    that can rapidly use members of this class.
    
    I'll need to set up a "check for archive" method
    to try and clear the old records out.
    """
    pass
    __slots__ = [
        'log_path',
        'error_path',
        'archive_path',
        'line_ending',
        'date_format',
        'name_format',
        'archive_at_size',
        'archive_count',
        'extension'
    ]
    def __init__(self,log_path = None, error_path = None, archive_path = None, line_ending = None, date_format = None, name_format = None, archive_at_size = None, archive_count = None):
        """
        initialize instance.
        """
        pass
        self.log_path = log_path or "./events.log"
        self.error_path = error_path or "./error.log"
        self.archive_path = archive_path or "./log_archive";
        self.line_ending = line_ending or "\r\n";
        self.date_format = date_format or "%Y-%m-%d %H:%M";
        self.name_format = name_format or "%Y-%m-%d_%s"; # %s will represent the filename.
        self.archive_at_size = archive_at_size or 10000; # 10000 bytes will probably be an adequate size, can be adjusted easily enough, no?
        self.archive_count = archive_count or 100; # use this to truncate the oldest files (might need to add an integration point to my analytic tools.)
    
    def write_(self,contents =None,log_path=None, is_error=None):
        """
        write data into the designated log.
        """
        pass
        n = datetime.datetime.now().strftime(date_format)
