# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# ask the user for input
text = input("Enter text: ")
# create a list of uppercase letters
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# create a list of lowercase letters
lowercase = "abcdefghijklmnopqrstuvwxyz"
# initialize an empty string to store the output
result = ""

# check if character is in the list of lowercase
for char in text:
    if char in lowercase:
        index = lowercase.index(char)    # if yes, find the position of that lowercase using index 
        result += uppercase[index]
    else:
        result += char  # if no, just store the already uppercase letter in the empty string
# print output
print(result)