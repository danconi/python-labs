# Read up on `range()` and additional options for `print()`.
# Then use a loop to print the following table to the console:
#
# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49


from turtle import end_fill


row = 5
# for num in range(1,row+1):
#     print (1,2,3,4end='')

for num in list(range(0,10)):
    print (num,end='')
    

for num in list(range(10,20)):
    print (num,end='')
    
