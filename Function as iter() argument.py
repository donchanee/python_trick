def seek_next_line(f):
    for c in iter(lambda: f.read(1),'\n'):
        pass


# The iter(callable, until_value) function repeatedly calls callable and yields its result until until_value is returned.
