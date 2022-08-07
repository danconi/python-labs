# Replace all occurrences of the letter `m` with the symbol `_`.
# For example:

# text: more python programming please
# symbol: #
# result: #ore python progra##ing please

poem = """10

maggie and milly and molly and may
went down to the beach(to play one day)

and maggie discovered a shell that sang
so sweetly she couldn't remember her troubles,and

milly befriended a stranded star
whose rays five languid fingers were;


S="plumage"
S

and molly was chased by a horrible thing
which raced sideways while blowing bubbles:and

may came home with a smooth round stone
as small as a world and as large as alone.

For whatever we lose(like a you or a me)
it's always ourselves we find in the sea"""

# Write your code below here


#greeting="hello"

#greeting_backwards = greeting[-1] + greeting[-2] + greeting[-3] + greeting[-4] + greeting[-5]

#print(greeting_backwards)




poem_edited = poem.replace("m","_")
print(poem_edited)