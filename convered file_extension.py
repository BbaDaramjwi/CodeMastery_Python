""" convered file_extension

    This script changes the file extension of a file.
    All files in the folder with the corresponding ending will be changed,
    this allows multiple files to be "convered" at the same time. 
    Choose your mode 1 or 2 and hit enter.
"""


import os


current_directory = os.path.dirname(os.path.realpath(__file__ ))

folder_path = os.path.join(current_directory)

formatting = "_________________________________________________\n"


def txt_to_md():
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt') and filename != "ReadMe.txt":
            source = os.path.join(folder_path, filename)
            target = os.path.join(folder_path, filename[:-4] + '.md')
            os.rename(source, target)


def md_to_txt():
    for filename in os.listdir(folder_path):
        if filename.endswith('.md') and filename != "ReadMe.txt":
            source = os.path.join(folder_path, filename)
            target = os.path.join(folder_path, filename[:-4] + '.txt')
            os.rename(source, target)


user_input = (input(
    f"\n{formatting}"
    f"\n Welcome Master,"
    f"\n Please select one of the following options below, hit enter"
    f"\n and I will change the file extension for you.\n"
    f"\n 1 | txt ---> md"
    f"\n 2 | md  ---> txt"
    f"\n \n >> "        ))


try:
    user_input = int(user_input)
    
    if user_input == 1:
        run = txt_to_md()
        print(f" >> txt ---> md is DONE")
        print(formatting)
        
    elif user_input == 2:
        run = md_to_txt()
        print(" >> md ---> txt is DONE")
        print(formatting)
    
    else:
        print(f"\n !!! Your input does not match the required input !!!")
        print(formatting)
        
except ValueError:
    print(f"\n !!! Your input does not match the required input !!!")
    print(formatting)