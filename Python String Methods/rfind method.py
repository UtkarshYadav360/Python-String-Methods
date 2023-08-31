# rfind method :
# finds the last occurence of the specified value.
# return -1 if the value is not found.

# ARGUMENTS :
# value : Required. The value to search for.
# start : Optional. Where to start the search. Default is  0.
# end : Optional. Where to end the search. Default is end of the string.

text = "Programming in Python is fun!"
print(text.rfind("n"))
print(text.rfind("Z"))

print(text.rfind("n", 14, 21))
