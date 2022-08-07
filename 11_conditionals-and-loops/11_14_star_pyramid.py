# Write a script that prints a star pyramid of flexible size
# If the `stars` variable is `5`, your code will output:
#
# *
# * *
# * * * 
# * * * *
# * * * * * 
#
# There should be five rows in total:
# 1. the 1st row will have 1 star,
# 2. the 2nd row will have 2 stars,
# 3. the 3rd row will have 3 stars,
# 4. the 4th row will have 4 stars,
# 5. the 5th row will have 5 stars
#
# Another example: if you set the `stars` variable tp `3`, 
# your code will output:
#
# *
# * *
# * * *
#
# HINT: Think of nested for loops!

# Pyramid_Size = 5
# string = ""
# space_string = ""
# print_string = ""
# for x in range(0,Pyramid_Size+1):
#     spaces = Pyramid_Size - x
#     for a in range(1,spaces+1):
#         space_string = space_string + " "
#     for y in range(1,x + 1):
#         string = string + "**"
#     print_string = space_string + string
#     print(print_string)
#     string = ""
#     space_string = ""





star=15

range_star=range(1,star)

for i in range_star:
    if i%2==0:
        print(i)
    else:
        print("not even ",i)


for i in range_star:
    print('*'*i)
for i in range(star,0,-1):
    print('*'*i)


    
