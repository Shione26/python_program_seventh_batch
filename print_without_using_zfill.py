# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# ask the user for input
string = str(input("Enter string: "))
# ask the user for the total number of characters
total_char = int(input("Enter total number of characters: "))
# subtract the length of the string to the total number of characters to get the zeroes
zeroes = total_char - len(string)
# concatenate the zeroes and the string
result = "0" * zeroes + string
# print output
print(result)