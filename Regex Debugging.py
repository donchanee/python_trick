# Regular expressions are a great feature of python, but debugging them can be a pain, and it's all too easy to get a regex wrong.

# Fortunately, python can print the regex parse tree, by passing the undocumented, experimental, 
# hidden flag re.DEBUG (actually, 128) to re.compile.

>>> re.compile("^\[font(?:=(?P<size>[-+][0-9]{1,2}))?\](.*?)[/font]",
    re.DEBUG)
at at_beginning
literal 91
literal 102
literal 111
literal 110
literal 116
max_repeat 0 1
  subpattern None
    literal 61
    subpattern 1
      in
        literal 45
        literal 43
      max_repeat 1 2
        in
          range (48, 57)
literal 93
subpattern 2
  min_repeat 0 65535
    any None
in
  literal 47
  literal 102
  literal 111
  literal 110
  literal 116

# Once you understand the syntax, you can spot your errors. There we can see that I forgot to escape the [] in [/font].

# Of course you can combine it with whatever flags you want, like commented regexes:

>>> re.compile("""
 ^              # start of a line
 \[font         # the font tag
 (?:=(?P<size>  # optional [font=+size]
 [-+][0-9]{1,2} # size specification
 ))?
 \]             # end of tag
 (.*?)          # text between the tags
 \[/font\]      # end of the tag
 """, re.DEBUG|re.VERBOSE|re.DOTALL)
