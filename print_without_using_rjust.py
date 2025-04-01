# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.'

# ask the user for input
text = str(input("Enter text: "))
# ask the user for the width
width = int(input("Enter width: "))
# compute the number of spaces to be filled at the beginning
spaces = width - len(text)
# concatenate the spaces and the text
result = " " * spaces + text
# print the result
print(f"'{result}'")