# rstrip method :
# removes any trailing characters (characters at the end of the string), space is default trailing character to remove.

# ARGUMENTS :
# characters :Optional. A set of characters to remove as trailing character.

text = "        Python         "
print(text)
print(text.rstrip())

new_text = "    Python,,,,----+++###"
print(new_text)
print(new_text.rstrip("-+#"))
