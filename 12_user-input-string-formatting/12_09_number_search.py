# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.


user_input1 = input('Enter a number between 0 and 1,000,000,000: ')

findnumber = 0
while findnumber != int(user_input1):
    if findnumber == int(user_input1):
        findnumber = int(user_input1)
    findnumber = findnumber + 1
print(findnumber)