>>> NewType = type("NewType", (object,), {"x": "hello"})
>>> n = NewType()
>>> n.x
"hello"

# which is exactly the same as

>>> class NewType(object):
>>>     x = "hello"
>>> n = NewType()
>>> n.x
"hello"
