# find method :
# finds the first occurence of the specified string.
# return -1 if the value if not find.

# ARGUMENTS :
# value : Required. The value to search for.
# start : Optional. Where to start the search. Default is 0.
# end : Optional. Where to end the search. Default is to the end of the string.

text = "Programming in Python is fun!"
print(text.find("m"))
print(text.find("Z"))

print(text.find("n", 14, 21))
