# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4


#from functools import update_wrapper


user_input1 = input("enter a string: ")
user_input2 = input("enter a single letter: ")
# index = user_input1.find(user_input2)
# if index == -1:
#     print("\nLetter Not Found\n")
# else:
#     print("\nLetter found at index: ",index,"\n")

print(user_input1.find(user_input2))

