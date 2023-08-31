# startswith method :
# return True if the string starts with the specified value, otherwise False.

# ARGUMENTS :
# value : Required. The value to check if the string starts with.
# start : Optional. An integer specifying at which position to start the search.
# end : Optional. An integer specifying at which position to end the search.

text = "Programming in Python is fun!"
print(text.startswith("P"))
print(text.startswith("p"))

print(text.startswith("P", 15, 20))
