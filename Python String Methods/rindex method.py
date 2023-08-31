# rindex method :
# finds the last occurence of the specified value.
# raise an exception error if the value is not found.

# ARGUMENTS :
# value : Required. The value to search for.
# start : Optional. Where to start the search. Default is 0.
# end : Optional. Where to end the search. Default is end of the string.

text = "Programming in Python is fun!"
print(text.index("n"))
# print(text.index("Z"))

print(text.index("n", 14, 21))
