# replace method :
# replace a specified phrase with another specified phrase.

# ARGUMENTS :
# old value : Required. The string to search for.
# new value : Required. The string to replace the old value with.
# count : Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences.

text = "I Loved Python!"
print(text.replace("Loved", "Love"))

new_text = "one one one one one two two two two five nine six"
print(new_text.replace("one", "seven", 4))
