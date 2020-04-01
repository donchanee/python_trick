>>> print "The %(foo)s is %(bar)i." % {'foo': 'answer', 'bar':42}
The answer is 42.

>>> foo, bar = 'question', 123

>>> print "The %(foo)s is %(bar)i." % locals()
The question is 123.

# And since locals() is also a dictionary, you can simply pass that as a dict and 
# have % -substitions from your local variables. I think this is frowned upon, but simplifies things..

# New Style Formatting

>>> print("The {foo} is {bar}".format(foo='answer', bar=42))
