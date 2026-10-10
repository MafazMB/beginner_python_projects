import os
import shutil



#edit so that user can type in file name and code automatically fetches dir path done
#create a folder for every item in extension
#add more sorting options such as based on date and name
#make current and new sorts as functions
def req_dir(path:str):
    global new_dir
    actual_path=os.path.abspath(path)
    os.chdir(actual_path)
    new_dir=os.getcwd()
    print(f"New dir: {new_dir}")

req_dir("Desktop")


extensions=[
    'pdf',
    'jpeg',
    'pptx',
    'HEIC',
    'png'
]






files=os.listdir(new_dir)
for file in files:
    for extension in extensions:
        if file.endswith(extension):
            print(extension, file)


