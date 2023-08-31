# strip method :
# removes any leading and trailing spaces from  the string.

# ARGUMENTS :
# characters : Optional. A set of characters to remove as leading/trailing characters.

text = "    Python      "
print(text)
print(text.strip())

new_text = ",,,ppqqtt...Python...pp"
print(new_text)
print(new_text.strip(",pqt."))
