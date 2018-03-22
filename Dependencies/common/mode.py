def mode(set):
    """
    analyze a set and return the mode of the set.
    I'll add in a function to display the count.
    *should* function well in python 2 and python 3
    since it doesn't rely on any quirks of either language.
    
    by default will throw errors if there is an equally frequent
    value in the dataset. This might cause an issue, so you should
    override it on your own time.
    
    replicates the behaviour of python 3's statistics.mode function,
    with the exception that this raises a general Exception vs
    StatisticsError.
    """
    if type(set) != list: raise TypeError("Input must be a list");
    data= {}
    no_mode = False
    re_ =  None
    for a in set:
        if a in data.keys():
            data.update({a:data[a]+1})
        else:
            data.update({a:1})
    for a in data.keys():
        #print("%s: %s"%(a,data[a])) # just for kicks.
        if re_ is None: 
            re_ = a
            continue;
        if data[a] == data[re_]: no_mode = True;
        if data[a] > data[re_]: 
            re_ = a
            no_mode = False
    #if no_mode: re_ = None;
    if no_mode: raise Exception("Found no mode, found at least two equally occurring values");
    return re_;