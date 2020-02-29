
#Decorators

#Decorators allow to wrap a function or method in another function that can add functionality, modify arguments or results, etc. You write decorators one line above the function definition, beginning with an "at" sign (@).

#Example shows a print_args decorator that prints the decorated function's arguments before calling it:

>>> def print_args(function):
>>>     def wrapper(*args, **kwargs):
>>>         print 'Arguments:', args, kwargs
>>>         return function(*args, **kwargs)
>>>     return wrapper

>>> @print_args
>>> def write(text):
>>>     print text

>>> write('foo')
Arguments: ('foo',) {}
foo
