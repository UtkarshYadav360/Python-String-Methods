# rsplit method :
# splits a string into list, starting from the right.

# ARGUMENTS :
# seperator : Optional. Specifes the seperator to use when splitting the string. By default any whitespace is a seperator.
# maxsplit : Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences".

text = "Programming in Python is fun!"
print(text.rsplit())

new_text = "Programming, in Python is, fun!"
print(new_text.rsplit(",", 1))
