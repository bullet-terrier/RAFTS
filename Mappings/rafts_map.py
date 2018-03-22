"""
Benjamin Tiernan

rafts_map.py

File containing the mapping elements for the RAFTS process to push files.

format will be of the following form: {<expected_input_arg>:{
    'host':'destination_name',
    'file':'file_path_to_load',
    'user':'username_to_pass',
    'pass':'password_to_use'    
    }
    }
    
This will translate to the cron call as:
* * * * * root RAFTS.py <expected_input_arg> 

which would then kick off the ftp process.
"""

library = {
    # here is a test entry. the scheduling will be handled at a separate location.
    # as well as any cleanup after the fact.
    "test":{'file':"C:/Local_Code/test_file.txt",'host':"localhost"}
   ,"test1":{'file':"C:/Local_Code/test_file - Copy.txt",'host':"localhost"}
}
