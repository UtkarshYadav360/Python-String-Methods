# format method :
# formats the specified value and insert them inside the string's placeholder.
# placeholder is defined using the curly braces {}.
# placeholders can be identified using {named indexes}, {numbered indexes}, empty placeholders{}.

# ARGUMENTS :
# value1, value2 .... : Required. One or more values that shuold be formatted and inserted in the string. Values can be of any data type.


text1 = "Programming in {language} is fun!".format(language="Python")
print(text1)


text2 = "Programming in {0} is {1}!".format("Python", "fun")
print(text2)


text3 = "Programming in {} is {}!".format("Python", "fun")
print(text3)
