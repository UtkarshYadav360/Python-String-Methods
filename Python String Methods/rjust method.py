# rjust method :
# right align the string, using a specified character (space is default) as the fill character.

# ARGUMENTS :
# length : Required. The lenght of the returned string.
# character : Opotional. A character to fill the missing space (to the left of the string). Default is space.

text = "Python"
print(text.rjust(20))
print(text.rjust(20, "-"))
