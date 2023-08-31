# isnumeric method :
# returns True if all the characters in the string are numeric 0-9, otherwise False.
# decimal values and negative are not considered as numbers as they have ("-" not number) and ("." not number)
# exponents are considerd as numberic values.


text1 = "345"
print(text1.isnumeric())

text2 = "-46"
print(text2.isnumeric())

text3 = "1.5"
print(text2.isnumeric())

text4 = "Hello12"
print(text4.isnumeric())
