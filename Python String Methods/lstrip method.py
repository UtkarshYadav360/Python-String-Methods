# lstrip method :
# removes any leading characters (space is the default leading charater to remove.) from left side.

# ARGUMENTS :
# characters : Optional. A set of characters to remove as leading characters.

text = "        Python      "
print(text)
print(text.lstrip())

new_text = ",,,,,sssaaawww.....Python"
print(new_text)
print(new_text.lstrip(",saw"))
