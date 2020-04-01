for i in foo:
    if i == 0:
        break
else:
    print("i was never 0")

#The "else" block will be normally executed at the end of the for loop, unless the break is called.

#The above code could be emulated as follows:

found = False
for i in foo:
    if i == 0:
        found = True
        break
if not found: 
    print("i was never 0")
