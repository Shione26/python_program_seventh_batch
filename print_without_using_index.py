# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

# ask the user for input
text = input("Enter text: ")
# ask the user what word to find
word = input("Enter word to find: ")
# using find(), find the first occurence of word in text
result = text.find(word)
if result == -1:
    print("-1")     # if not found, print -1
else:
    print(result)   # otherwise, print position