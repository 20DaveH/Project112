import os
import shutil

from_dir = "C:/Users/Preetesh/Downloads"
to_dir = "C:/Users/Preetesh/Documents"

list_of_files = os.listdir(from_dir)
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir+'/'+ file_name
        path2 = to_dir+'/'+"image_files"
        path3 = to_dir+'/'+"image_files"+'/'+file_name
        if os.path.exists(path2):
            shutil.move(path1,path3)
            print("Moving ",file_name," ...")

        else:
            os.mkdir(path2)
            shutil.move(path1,path3)
            print("Moving ",file_name," ...")