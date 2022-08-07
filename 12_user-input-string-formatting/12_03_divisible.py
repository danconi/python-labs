# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

user_input1 = input("enter a number between 1 and 1,000,000,000: ")

if int(user_input1)%3 == 0:
    print("your numer is divisible by 3")

if int(user_input1)%3 != 0:
    print("your numer is not divisible by 3")


