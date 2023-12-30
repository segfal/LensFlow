
import os, shutil,time ,PIL,datetime

def file_filter(file_list, file_extension):
    """
    Filter a list of files by file extension.

    Parameters:
    - file_list: A list of strings representing the filenames.
    - file_extension: A string representing the file extension to filter by.

    Returns:
    - A list of strings representing the filtered filenames.
    """
    filtered_files = []
    for file in file_list:
        if file.endswith(file_extension):
            filtered_files.append(file)
    return filtered_files


#store the filtered files into a folder
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

