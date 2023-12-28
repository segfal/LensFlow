from File_Functions import file_exists,metadata,file_filter,file_mover

pathOfUSB = ""
pathOfPics = ""

def get_usb_drives():
    drive_list = []
    for partition in psutil.disk_partitions():
        if 'removable' in partition.opts:
            drive_list.append(partition.mountpoint)
    return drive_list

# Now let's assume the first removable drive is the USB you want to use
usb_drives = get_usb_drives()
if usb_drives:
    REMOVABLE_USB_PATH = usb_drives[0]
else:
    REMOVABLE_USB_PATH = None  # Handle the case where no USB is found
