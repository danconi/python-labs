
# c = input(" ")
# temp = {}
# output = " "
# for x in c:
#     if x in temp:
#         temp[x] = temp[x] + 1
#     else:
#         temp[x] = 1
# for key, value in temp.items():
#     output += str(value) + str(key)
# print(output)
spaces = []

for x in range(0,len(CN)):
    if CN[x] == " ":
        spaces.append(x)
initial = 0
end = 0
words = []
for x in range(0,len(spaces)):
    if x == 0:
        words.append(CN[1:spaces[x]])
        initial = spaces[x]
    elif x == len(spaces) - 1:
        words.append(CN[spaces[x]+1: len(CN) - 1])
    else:
        words.append(CN[spaces[x-1]+1:spaces[x]])
        initial = spaces[x]
pig_words = []
for x in words:
   pig = x[1:len(x)] + x[0:1] + "ay"
   pig_words.append(pig)

pig_story = ""
for x in pig_words:
    pig_story = pig_story + " " + x

print(pig_story)