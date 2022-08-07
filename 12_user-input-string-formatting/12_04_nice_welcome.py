# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.


user_input1 = input("enter your name: ")

if user_input1[0] == " ":
    user_input1 = user_input1[1:]

if user_input1.find(" ") != -1:
    print("Welcome "+ user_input1[0:user_input1.find(" ")])
else:
    print("Welcome "+ user_input1)



