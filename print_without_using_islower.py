# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# ask the user for input
text = input("Enter text: ")
# define lowercase characters
lowercase = "abcdefghijklmnopqrstuvwxyz"
# check manually if all characters is on lowercase
for char in text:
    if char not in lowercase:
        print("False")  # if no, print False
        break
# if yes, print True
else:
    print("True")