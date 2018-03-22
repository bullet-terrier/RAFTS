# parse input as list

def strip_brackets(string):
    """
    """
    if '[' and ']' in string:
        string = string.replace("[","").replace("]","")
    return string;

def str2list(stringin):
    """
    convert a formatted string into a list (based on how python should see it>)
    """
    stringin = strip_brackets(stringin);
    stringin = stringin.replace('"',"");
    stringin = stringin.replace("'","");
    stringin = stringin.split(','); # now it should be a list.
    return stringin
    