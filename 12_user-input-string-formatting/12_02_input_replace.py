# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please



user_input1 = input("enter a string: ")
user_input2 = input("enter a symbol: ")

print(user_input1.replace(user_input1[0],user_input2))