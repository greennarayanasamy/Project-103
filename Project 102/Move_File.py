import shutil
import os

from_dir="C:/Users/Samy/Downloads"
to_dir="C:/Users/Samy/Documents/Coding/Document_Files"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension=os.path.splitext(file_name)
    #prints the name of the file
    print(name)
    #prints the extension type of the file e.g. doc or py
    print(extension)

    #Checks if Folder/Directory Path exists before moving
    #Else creates a NEW Folder/Directory then moves
    if extension==" ":
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
       path1 = from_dir + "/" + file_name
       path2 = to_dir + "/" + "Document_Files"
       path3 = to_dir + "/" + "Document_Files" + "/" + file_name
       
       if os.path.exists(path2):
        print("Moving" + file_name + ".....")

        #Moves file from path 1 to path 3
        shutil.move(path1,path3)
        
       else: 
        os.makedirs(path2)
        print("Moving" + file_name + ".....")
        shutil.move(path1,path3)