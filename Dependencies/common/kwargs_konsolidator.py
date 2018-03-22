#
"""
Benjamin Tiernan

2018-03-21

Unit to help deal with keyword-based
argument parameters. This will allow 
us to utilize more robust features
in various functions.

usage: from kwargs_konsolidator import * (name needs some work)

contents:
  reconcile: merge two dictionaries, such as kwargs.

"""


#
# CONVENTIONS FOR HANDLING KWARGS
# 1) generate a base dictionary that contains the data
# 2) reconcile the differences in **kwargs and this dict.
# 3) utilize the base dict[key] as the template to control
#    your process.
# 4) enjoy faster, and cleaner development.
#
#

def reconcile(dict_1, dict_2):
    """
    update dict_1 withe the contents of dict_2;
    """
    pass
    for a in dict_2.keys():
        dict_1.update({a:dict_2[a]});
    del dict_2;
    return dict_1;

# defining a common dict that can be imported to serve as 
# a placeholder for a kwarg dictionary. Someone might find this 
# useful... i guess...
# what's a few more bytes, no?
common_dict = {
    "file":"",
    "user":"",
    "pass":"",
    "verb":"",
    "-v":"",
    "-i":"",
    "-o":"",
    "opts":"",
    "data":"",
    "conn":"",
    "curs":"",
    "arg":"",
    "var":"",
    "src":""
}
    
if __name__=="__main__":
    print("I'm not sure why...")
else:
    print("Nice - looks like you're intending to kwargparse lol")