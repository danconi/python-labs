# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib


a = pathlib.Path().cwd()
a = a.joinpath("Documents\\Codingnomads\\python-101-main\\13_modules-and-automation")
pyfile = []

print("\n\n Python files in Folder: ",a.name,"\n")
for file in a.iterdir():
    if file.suffix == ".py":
        print(file.name)
        
















#pathlib.Path().cwd() 
# os.chdir("Documents")
# Current_Directory = pathlib.Path.cwd()
# Directories = []
# Files = []



# Contents = Current_Directory.iterdir()
# Contents_list = []
# for child in Contents:
#     Contents_list.append(str(child))

# for child in Contents_list:
#     tempPath = Current_Directory.joinpath(child)
#     if tempPath.is_dir():
#         Directories.append(tempPath.name)
#     else:
#         if tempPath.suffix == ".py":
#             Files.append(tempPath.name)
# print(Contents[0])
# #### PRINT STATEMENTS

# print("\nDIRECTORIES:")
# for p in Directories:
#     print(p)
# print("\nFILES:")
# for f in Files:
#     print(f)
# print("\n")


# print("\n\n",Curr,"\n\n")
# print(Contents_list[0])

# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there