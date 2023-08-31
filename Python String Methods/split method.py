# split method :
# split the string into a list.

# ARGUMENTS :
# seperator : Optional. Specifies the seperator to use when splitting the string. By default any whitespace is a seperator.
# maxsplit : Optional. Specifies how many splits to do. Default value  is -1 which is "all occurrences".

text = "Programming in Python is fun!"
print(text.split())

new_text = "Programming#in#Python#is#fun!"
print(new_text.split("#", 1))
