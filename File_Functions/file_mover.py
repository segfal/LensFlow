import os, shutil,time,datetime

def move_files(source, destination):
    files = os.listdir(source)
    for f in files:
        shutil.move(os.path.join(source, f), destination)

'''move_files("./", "./test/")'''

''' Format for Folder names, MM.DD.YYYY
ex.) 12.20.2023, 05.03.2022, etc. '''


