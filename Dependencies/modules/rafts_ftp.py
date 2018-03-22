#!##PYTHONPATH##
"""
Benjamin Tiernan
2018-03-20

Module to contain logic dictating how the ftp files should be sent.
This will mostly depend on which platform the command is running on,
as well as the available os tools.

Should basically be blind to most input and output, primarily relying
on being imported as an extension module.
"""

import platform;
import ftplib;
import os;
import sys;
# Looks like I'm not going to worry too much about windows support, 
# I'll include the precursors so we could generate it in a pinch.
# 

def ftp_script_help():
    """
    help message for the ftp_script function.
    """
    sys.stdout.write("""
        args:
            host : site to connect to
            user : username to use
            pass : password to use
            file : file to put
            directory : directory to put file into
            
        implementation:
            connet(server)
            login()
            ftp.cwd()
            ftp.storlines('STOR./%s'%(sourcepath);
            --> handle the termination tasks.
        returns error code or any other messages.
    \n"""
    )
    return;

def ftp_script(**args):
    """
    ## SEE ftp_script_help() ##
    ## DOCUMENTATION MOVED   ##
    """
    key_list = []
    has_file = False;
    has_user = False;
    has_pass = False;
    has_dire = False;
    has_host = False;
    pass_creds = False;
    return_message = None;
    has_exception = False;
    # stronger version would be to handle a variety of args, but
    # I don't feel like putting forth the effort to do that in this
    # limited scope.
    #
    # We'll be able to expand and encode more information 
    for a in args.keys():
        if a is "host":
            pass
            has_host=True;
        if a is "user":
            pass
            has_user=True;
            pass_creds = True;
        if a is "file":
            pass
            has_file = True;
        if a is "directory":
            pass
            has_dire = True;
        if a is "pass":
            pass
            has_pass = True;
            pass_creds = True;
    if not has_host: 
        ftp_script_help();
        has_exception = True;
        raise Exception("Host must be specified.");
    if pass_creds and not has_user: 
        ftp_script_help();
        has_exception = True;
        raise Exception("If a password is specified, you must specify a user.");
    try:
        ftp = ftplib.FTP()
        ftp.connect(args['host']);
        if not pass_creds: ftp.login();
        else: ftp.login(user=args['user'],passwd=args['pass'])
        # store the file- by name and with a binary representation of the file.
        message = ftp.storlines('STOR %s'%(os.path.basename(args['file'])),open(args['file'],'rb'));
    except Exception as E:
        return_message = str(E);
        has_exception = True;
    return return_message,has_exception;