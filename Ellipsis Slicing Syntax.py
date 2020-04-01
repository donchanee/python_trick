>>> class C(object):
...  def __getitem__(self, item):
...   return item
... 
>>> C()[1:2, ..., 3]
(slice(1, 2, None), Ellipsis, 3)
