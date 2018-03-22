# RAFTS

Benjamin Tiernan
2018-03-20

python program to facilitate centralized and automated FTP emission.

Will provide 'hard points' that will facilitate the use of the infividual mappings 
and allows for the derivation of other processes from it's data structure.

Runs interchangeably on linux and windows, but requires the "#!##PYTHONPATH##" expression
to be changed to represent the path to the desired python interpreter.

this can also be done by calling the interpreter, then the program ie:
"python RAFTS.py arg1 arg2" etc.

# CONFIGURATION

rafts_heartbeat is an optional module that should allow persistence monitoring for the processes.
the PC must be continuously on for it to function, and will need to be restarted if the machine goes down.

configure alert timing, file locations and alert lists in the header of the file (for now).

mapping for RAFTS can be handled in the "Mappings" directory and will include further instructions
for sending automated FTP utilities.

Lastly, there will be a cron template included for the user's convenience.