import os

def check_folder_exists(date_folder, base_directory):
    """
    Check if a folder with the given date exists in the base directory.

    Parameters:
    - date_folder: A string representing the folder name in the format "MM.DD.YYYY"
    - base_directory: A string representing the path to the base directory where folders are stored.

    Returns:
    - True if the folder exists, False otherwise.
    """
    # Construct the full path to the date folder
    full_path = os.path.join(base_directory, date_folder)
    
    # Check if the directory exists
    return os.path.isdir(full_path)

# Example usage:
# exists = check_folder_exists("12.27.2023", "path/to/pictures/directory")
# print(f"Does the folder exist? {exists}")


def check_file_exists(filename, directory):
    """
    Check if a file with the given filename exists in the specified directory.

    Parameters:
    - filename: A string representing the name of the file.
    - directory: A string representing the path to the directory where the file is expected.

    Returns:
    - True if the file exists, False otherwise.
    """
    # Construct the full path to the file
    full_path = os.path.join(directory, filename)

    # Check if the file exists
    return os.path.isfile(full_path)

# Example usage:
# exists = check_file_exists("filename", "path/to/pictures/directory")
# print(f"Does the folder exist? {exists}")

