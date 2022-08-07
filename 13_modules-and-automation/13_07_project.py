#File Search
Write a script that searches a folder you specify (as well as its subfolders, up to two levels deep) and compiles a list of all .jpg files contained in there. The list should include the complete path of each .jpg file.

You should train:

Using for loops
Using conditional statements
Working with pathlib
Thinking about nested loops
If you are feeling bold, create a list containing each type of file extension you find in the folder.

Start with a small folder to make it easy to check whether your program is working correctly. Then search a bigger folder.

This program should work for any specified folder on your computer.

import pathlib


a = pathlib.Path().cwd()
a = a.joinpath("Documents\\Codingnomads")
pyfile = []

print("\n\n Python files in Folder: ",a.name,"\n")
for file in a.iterdir():
    if file.is_dir():
        temp = "\n" + file.name.upper() + ":"
        pyfile.append(temp)
        for file1 in file.iterdir():
            if file1.is_dir():
                temp = "\t|__" + file1.name.upper() + ":"
                pyfile.append(temp)
                for file2 in file1.iterdir():
                    if file2.suffix == ".py":
                        temp = "\t\t\t|__" + file2.name
                        pyfile.append(temp)
            elif file1.suffix == ".py":
                temp = "\t\t|__" + file1.name
                pyfile.append(temp)

    elif file.suffix == ".py":
        pyfile.append(file.name)

for py in pyfile:
    print(py)

# print(a)
















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