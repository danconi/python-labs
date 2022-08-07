# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

user_input1 = input('Enter a number: ')

months = [" ","january","february","march","april","may","june","july","august","september","october","november","december"]

if int(user_input1) > 12 or int(user_input1) < 1:
    print("Error!!! Only twelve months dumbass!!!")
else:
    print(months[int(user_input1)])

    



