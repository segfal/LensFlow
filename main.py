'''from psysort/File_Functions import file_exists,metadata,file_filter,file_mover
'''
import psutil

PICTURES_LIBRARY_PATH = "F:\Pictures\Raws"
REMOVABLE_USB_PATH = None  

def get_usb_drive():
    global REMOVABLE_USB_PATH
    drive_list = []
    for partition in psutil.disk_partitions():
        if 'removable' in partition.opts:
            drive_list.append(partition.mountpoint)
    if drive_list:
        REMOVABLE_USB_PATH = drive_list[0]
        
usb_drives = get_usb_drive()

def some_function():
    # You can use the global variables here
    print(f"Accessing pictures library at {PICTURES_LIBRARY_PATH}")
    if REMOVABLE_USB_PATH:
        print(f"Accessing removable USB at {REMOVABLE_USB_PATH}")
    else:
        print("No removable USB drive found.")

print(f"Removable USB Path Set To: {REMOVABLE_USB_PATH}")

# Now let's assume the first removable drive is the USB you want to use
if usb_drives:
    REMOVABLE_USB_PATH = usb_drives[0]
else:
    REMOVABLE_USB_PATH = None  # Handle the case where no USB is found


