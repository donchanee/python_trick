def mygen():
    """Yield 5 until something else is passed back via send()"""
    a = 5
    while True:
        f = (yield a) #yield a and possibly get f in return
        if f is not None: 
            a = f  #store the new value

# You can:

>>> g = mygen()
>>> g.next()
5
>>> g.next()
5
>>> g.send(7)  #we send this back to the generator
7
>>> g.next() #now it will yield 7 until we send something else
7
