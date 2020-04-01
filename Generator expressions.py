# If you write

x=(n for n in foo if bar(n))
# you can get out the generator and assign it to x. Now it means you can do

for n in x:

# The advantage of this is that you don't need intermediate storage, which you would need if you did

x = [n for n in foo if bar(n)]

# In some cases this can lead to significant speed up.

# You can append many if statements to the end of the generator, basically replicating nested for loops:

>>> n = ((a,b) for a in range(0,2) for b in range(4,6))
>>> for i in n:
...   print i 

(0, 4)
(0, 5)
(1, 4)
(1, 5)
