# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

user_input1 = input("investment amount: ")
user_input2 = input("interest rate in percentage: ")
user_input3 = input("number of years to invest: ")

M = [float(user_input1) *((1+float(user_input2)*float(user_input3)))]

print(M)
