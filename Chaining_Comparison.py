# Chaining comparison operators:
>>> x = 5
>>> 1 < x < 10
True
>>> 10 < x < 20 
False
>>> x < 10 < x*10 < 100
True
>>> 10 > x <= 9
True
>>> 5 == x > 4
True

'''
 In case you're thinking it's doing 1 < x, which comes out as True, and then comparing True < 10, 
 which is also True, then no, that's really not what happens (see the last example.) 
 It's really translating into 1 < x and x < 10, and x < 10 and 10 < x * 10 and x*10 < 100, 
 but with less typing and each term is only evaluated once.
'''
