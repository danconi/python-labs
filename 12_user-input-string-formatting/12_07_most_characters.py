# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

user_input1 = input('Enter a string: ') 
user_input2 = input('Enter a string: ') 
user_input3 = input('Enter a string: ') 

maxlength = max(len(user_input1), len(user_input2), len(user_input3))

users = [user_input1, user_input2, user_input3]

for x in users:
    if len(x) == maxlength:
        print(x,maxlength)