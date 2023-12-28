import os, shutil,time ,PIL,datetime




def move_files(source, destination):
    '''
    Moves files from source to destination
    '''
    files = os.listdir(source)
    # sort files by date
    files.sort(key=os.path.getmtime)
    # move files
    for f in files:
        shutil.move(os.path.join(source, f), destination)



    

move_files("./", "./test/")

''' Format for Folder names, MM.DD.YYYY
ex.) 12.20.2023, 05.03.2022, etc. '''

