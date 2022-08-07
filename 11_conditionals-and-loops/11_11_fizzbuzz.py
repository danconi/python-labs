# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number


n = 100
output = ""

for x in range(1,n+1):
    if x%3 == 0 and x%5 == 0:
        #output = output + "FizzBuzz"
        print("FizzBuzz")
    elif x%3 == 0:
        #output = output + "Fizz"
        print("Fizz")
    elif x%5 == 0:
        #output = output + "Buzz"
        print("Buzz")
    else:
        #output = output + str(x)
        print(x)
#print(output)
    
