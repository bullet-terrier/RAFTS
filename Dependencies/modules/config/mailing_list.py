#!##PYTHONPATH##
"""
mailing_list.py

Benjamin Tiernan
2018-03-21

Part of the extended RAFTS software suite.
mechanism to extend heartbeat to multiple 
benchmarks and mailing lists.

entry format:
    {<report_name>:{'error':[<email_address>,<email_address>],'update':[<email_address>,<email_address>]}}
    
alternate entry format:
    {<report_name>:
      {'error':[<email_address>,<email_address>],
       'update':[<email_address,<email_address>]
      }
    }
"""

# exports the mail_list;
mail_list = {
    # replace these
    'test':{
        'error':['bullet-terrier@test.com'],
        'update':['bullet-terrier@test.com']
    },
    'rafts':{
        'error':['bullet-terrier@test.com'],
        'update':['bullet-terrier@test.com']
    }    
}

mail_list.default = 'test';

if __name__=="__main__":
    print("You shouldn't be executing this file - it is only designed to emit structured data.")
    help(__name__)
    input();
else:
    d = mail_list.keys();
    ls = ""
    for a in d: ls+= "%s\r\n"%(a);
    print("""
available objects:
    mail_list
    
available values:
    %s
    """%(ls))
