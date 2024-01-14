"""
    MVC - Model View Controller
    The MVC principle is an architectural pattern in software development
    that is used to organise the structure of applications.
    
    This script creates a corresponding folder structure :)
"""


import os

def new_projekt_MVC():

    script_path = os.path.dirname(os.path.abspath(__file__))

    folder_Main = "!!! NEW-Project !!!"

    folder_subM = "Model"
    folder_subV = "View"
    folder_subC = "Controller"

    txt_M = "ReadMe_Model.txt"
    txt_V = "ReadMe_View.txt"
    txt_C = "ReadMe_Controller.txt"

    if not os.path.exists(os.path.join(script_path, folder_Main)):

        os.mkdir(os.path.join(script_path, folder_Main))
        os.mkdir(os.path.join(script_path, folder_Main, folder_subM))
        os.mkdir(os.path.join(script_path, folder_Main, folder_subV))
        os.mkdir(os.path.join(script_path, folder_Main, folder_subC))

        with open(os.path.join(script_path, folder_Main, folder_subM, txt_M), 'w') as f: 
            f.write('Read me for ' + folder_subM)
        with open(os.path.join(script_path, folder_Main, folder_subV, txt_V), 'w') as f:
            f.write('Read me for ' + folder_subV)
        with open(os.path.join(script_path, folder_Main, folder_subC, txt_C), 'w') as f:
            f.write('Read me for ' + folder_subC)

        print("Done: The new project directory has been created")
    else:
        print("Failed: There is already a New project folder, which must be renamed")

create = new_projekt_MVC()