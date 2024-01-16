"""
    Editor-FileExtension
    This script changes the file extension of a file.
    All files in the folder with the corresponding ending will be changed,
    this allows multiple files to be renamed at the same time. 
    Choose your mode.
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


userInput = int(input(
    f"\n{formatting}"
    f"\n Welcome Master,"
    f"\n Please select one of the following options below"
    f"\n and I will change the file extension for you.\n"
    f"\n 1 | - txt -> md"
    f"\n 2 | -  md -> txt"
    f"\n "       ))

if userInput == 1:
    run = txt_to_md()
    print(f"txt_to_md - DONE {formatting}")
            
if userInput == 2:
    run = md_to_txt()
    print("md_to_txt - DONE")
        
    


