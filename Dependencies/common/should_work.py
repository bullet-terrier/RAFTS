import _ssl;
def t_pass(txt):
    ln = len(txt)
    bts = bytes(txt,'utf-8')
    ln = 2*len(bts)
    _n_ = []
    nuj = _ssl.RAND_bytes(2*ln)
    while len(bts)<ln: bts+=b'\x00'
    for a in range(0,len(bts)):
        _n_.append(bts[a]^nuj[a])
    return _n_,bts,nuj