# ljust method :
# left allign the string, using the specified character (space is default) as the fill character.

# ARGUMENTS :
# length : Required. The length of the returned string.
# character : Optional. A character to fill the missing space (to the right of the string). Default is space.

text = "Python"
left_lustified_string = text.ljust(20, "O")
print(left_lustified_string)
