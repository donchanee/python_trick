>>> class MyDict(dict):
...  def __missing__(self, key):
...   self[key] = rv = []
...   return rv
... 
>>> m = MyDict()
>>> m["foo"].append(1)
>>> m["foo"].append(2)
>>> dict(m)
{'foo': [1, 2]}

# There is also a dict subclass in collections called defaultdict that does pretty much the same 
# but calls a function without arguments for not existing items:

>>> from collections import defaultdict
>>> m = defaultdict(list)
>>> m["foo"].append(1)
>>> m["foo"].append(2)
>>> dict(m)
{'foo': [1, 2]}
