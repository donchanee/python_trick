# Function argument unpacking

# You can unpack a list or a dictionary as function arguments using * and **.

# For example:

def draw_point(x, y):
    # do some magic

point_foo = (3, 4)
point_bar = {'y': 3, 'x': 2}

draw_point(*point_foo)
draw_point(**point_bar)

# Very useful shortcut since lists, tuples and dicts are widely used as containers.
