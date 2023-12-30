import psutil

REMOVABLE_USB_PATH = None

def get_sd():
    global REMOVABLE_USB_PATH
    for partition in psutil.disk_partitions():
        if 'removable' in partition.opts:
            REMOVABLE_USB_PATH = partition.mountpoint
            return REMOVABLE_USB_PATH
    return None
