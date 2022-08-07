# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

user_input1 = input('whats your opinion about Trump: ')

for i in range(0,len(user_input1)):
    if i%2 == 0:
        user_input1[i].upper()
    else: 
        user_input1[i].lower()
print (user_input1)