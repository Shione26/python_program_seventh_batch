# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# ask the user for input
text = str(input("Enter text: ")) 
# inspect each character backwards from the end if it is a non-space character
for char in range(len(text) - 1, -1, -1):
    if text[char] != " ":
        break   # if found a non-space, break
# print output
print(f"'{text[:char + 1]}'")