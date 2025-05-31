import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_ext = filename.split('.')[-1]
        ext_folder = os.path.join(folder_path, file_ext.upper())
        if not os.path.exists(ext_folder):
            os.makedirs(ext_folder)
        shutil.move(os.path.join(folder_path, filename), os.path.join(ext_folder, filename))

folder = input("Enter the path of the folder to organize: ")
organize_files(folder)
print("Files organized by type!")
