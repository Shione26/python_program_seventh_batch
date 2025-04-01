# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# ask the user for input
text = input("Enter text: ")
# ask the user what word to find
word = input("Enter word to find: ")
# using rfind(), find the last occurrence of word in text
result = text.rfind(word)
if result == -1:
    print("-1")     # If not found, print -1
else:
    print(result)   # Otherwise, print position