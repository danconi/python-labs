# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
# re. findall()


# user_input1 = input("enter a string: ")
# user_input2 = input("enter a symbol: ")


VOWELS = 'aeioufgkasddaff'

user_input1 = input('Enter a string: ')

print_string = "Vowel counts\n"

count = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for x in VOWELS:
    count = user_input1.count(x)
    print_string = print_string + x + ": " + str(count) + "\n"

    if x == "a":
        count_a = count

    
print(print_string)
print(count_a)