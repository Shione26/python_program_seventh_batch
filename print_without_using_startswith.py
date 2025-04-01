# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# ask the user for input
text = input("Enter text: ")
# ask the user the prefix
prefix = input("Enter prefix: ")
# check if the prefix is at the beginning
if text [:len(prefix)] == prefix:
    print("True")   # if yes, print True
else:
    print("False")  # if no, print False