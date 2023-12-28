# main.py
from File_Functions import file_exists, metadata, file_filter, file_mover, get_usb_drive, PICTURES_LIBRARY_PATH

def main():
    # Initialize paths
    usb_drive_path = get_usb_drive()
    if not usb_drive_path:
        print("No USB drive found.")
        return
    
    # Your main code logic here

if __name__ == "__main__":
    main()
