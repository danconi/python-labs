# Print out every prime number between 1 and 1000.


for num in range(3,1001):
    #print("the outer num is: ",num)
    for othernum in range(2,num):
        if num%othernum==0:
            break
        else:
            print('prime,num ',num)
    
