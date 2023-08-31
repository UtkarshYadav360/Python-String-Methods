# endswith method :
# return True if the string ends with a specified value, otherwise False.

# ARGUMENTS :
# value : Required. The value to check if the string ends with.
# start : Optional. An integer specifying at which position to start the search.
# end : Optional : An integer specifying at which position to end the search.


text = "Programming in Python is fun!"
print(text.endswith("fun!"))
print(text.endswith("Fun!"))


print(text.endswith(" ", 11, 15))
print(text.endswith("P", 11, 15))
