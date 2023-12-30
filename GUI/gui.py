import os, shutil, datetime
import tkinter as tk
from tkinter import filedialog, messagebox, font as tkfont
from tkinter.ttk import Progressbar
from PIL import Image, ExifTags

def get_metadata(file_path):
    print() #print is a placeholder for where get_metadata implementation goes

def move_files_to_date_folder(source_folder, destination_folder):
    print() #print is a placeholder for where move files to date implementation goes

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def clear_warning(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Label) and "warning_label" in str(widget):
            widget.destroy()

def on_clear_checkbox_selected(frame, var):
    clear_warning(frame) # clears an existing warning
    if var.get():
        warning_label = tk.Label(frame, text="Warning: Your SD card files will be deleted!", fg="red", name="warning_label")
        warning_label.pack()
        messagebox.showwarning("Warning", "Your SD card files will be deleted!", parent=frame)

def update_stats(frame, path):
    clear_frame(frame)

    if path:
        dir_name = os.path.basename(path)
        file_count = sum([len(files) for r, d, files in os.walk(path)])
        total_size = sum([os.path.getsize(os.path.join(r, name)) for r, d, files in os.walk(path) for name in files])

        tk.Label(frame, text=f"Directory: {dir_name}", font="Helvetica 14 italic").pack()
        tk.Label(frame, text=f"Files: {file_count}", font="Helvetica 14 italic").pack()
        tk.Label(frame, text=f"Size: {total_size/1024/1024:.2f} MB", font="Helvetica 14 italic").pack()
        # can add more stats if you want
    else:
        tk.Label(frame, text="No directory selected", font="Helvetica 14 italic").pack()

def welcome_screen(frame):
    clear_frame(frame)
    welcome_font = tkfont.Font(family="Helvetica", size=24, weight="bold")

    # main (3/4 of the screen)
    main_content_frame = tk.Frame(frame)
    main_content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 2))

    separator_line = tk.Frame(frame, width=2, bg='gray')
    separator_line.pack(side=tk.LEFT, fill=tk.Y)

    # stats (1/4 of the screen)
    stats_frame = tk.Frame(frame)
    stats_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    label_welcome = tk.Label(main_content_frame, text="Welcome to PySort!\n", font=welcome_font)
    label_welcome2 = tk.Label(main_content_frame, text="Select your SD/USB or Detect Automatically.")
    label_welcome.pack()
    label_welcome2.pack()

    directory_frame = tk.Frame(main_content_frame)
    directory_frame.pack(pady=(5, 0))

    label_directory = tk.Label(directory_frame, text="Directory:")
    label_directory.pack(side=tk.LEFT)

    entry_sd_card_path = tk.Entry(directory_frame, width=30, bg='white', fg='black')
    entry_sd_card_path.pack(side=tk.LEFT, padx=5)

    button_browse = tk.Button(directory_frame, text="Browse", command=lambda: [browse_folder(entry_sd_card_path), update_stats(stats_frame, entry_sd_card_path.get())])
    button_browse.pack(side=tk.LEFT)

    bottom_frame = tk.Frame(main_content_frame)
    bottom_frame.pack(pady=(5, 0))

    checkbox_auto_detect_var = tk.BooleanVar()
    checkbox_auto_detect = tk.Checkbutton(bottom_frame, text="Detect Automatically", variable=checkbox_auto_detect_var)
    checkbox_auto_detect.pack(side=tk.LEFT, padx=10)

    button_next = tk.Button(bottom_frame, text="Next", command=lambda: output_directory_screen(frame, entry_sd_card_path.get(), checkbox_auto_detect_var.get()))
    button_next.pack(side=tk.LEFT)

    # initially no stats
    update_stats(stats_frame, "")


def output_directory_screen(frame, sd_card_path, auto_detect):
    clear_frame(frame)
    label_output_dir = tk.Label(frame, text="Select the Output Directory.", font = "Helvetica 24 bold")
    label_output_dir.pack()

    entry_frame = tk.Frame(frame)
    entry_frame.pack(pady=(5, 0))

    entry_output_dir_path = tk.Entry(entry_frame, width=30, bg='white', fg='black')
    entry_output_dir_path.pack(side=tk.LEFT, padx=(0, 5))

    button_browse_output_dir = tk.Button(entry_frame, text="Browse", command=lambda: browse_folder(entry_output_dir_path))
    button_browse_output_dir.pack(side=tk.LEFT)

    checkbox_frame = tk.Frame(frame)
    checkbox_frame.pack(pady=5)

    checkbox_create_subfolders_var = tk.BooleanVar()
    checkbox_create_subfolders = tk.Checkbutton(checkbox_frame, text="Create subfolders for different file types", variable=checkbox_create_subfolders_var)
    checkbox_create_subfolders.pack(side=tk.LEFT)

    checkbox_clear_usb_var = tk.BooleanVar()
    checkbox_clear_usb = tk.Checkbutton(checkbox_frame, text="Clear SD Card?", variable=checkbox_clear_usb_var, command=lambda: on_clear_checkbox_selected(frame, checkbox_clear_usb_var))
    checkbox_clear_usb.pack(side=tk.LEFT)

    button_sort = tk.Button(frame, text="Sort My Photos", command=lambda: sorting_screen(frame, sd_card_path, entry_output_dir_path.get(), checkbox_create_subfolders_var.get(), checkbox_clear_usb_var.get()))
    button_sort.pack(pady=5)


def sorting_screen(frame, sd_card_path, output_path, create_subfolders, clear_usb):
    clear_frame(frame)
    loading_font = tkfont.Font(family="Helvetica", size=24, weight="bold")

    label_sorting = tk.Label(frame, text="Sorting your images...", font = loading_font)
    label_sorting.pack()

    progress = Progressbar(frame, orient=tk.HORIZONTAL, length=200, mode='indeterminate')
    progress.pack(pady=10)
    progress.start()

    # for now it fakes the file sorting with a delay, replace this with actual sorting function call
    frame.after(2000, lambda: sorting_complete_screen(frame))

def sorting_complete_screen(frame):
    clear_frame(frame)
    complete_font = tkfont.Font(family="Helvetica", size=24, weight="bold")

    label_complete = tk.Label(frame, text="Sorting complete!", font = complete_font)
    label_complete.pack()

    restart_question = tk.Label(frame, text="Would you like to restart?")
    restart_question.pack()

    button_frame = tk.Frame(frame)
    button_frame.pack(pady=5)

    button_continue = tk.Button(button_frame, text="Yes", command=lambda: welcome_screen(frame))
    button_continue.pack(side=tk.LEFT, padx=5)

    button_cancel = tk.Button(button_frame, text="No", command=root.destroy)
    button_cancel.pack(side=tk.LEFT, padx=5)

def browse_folder(entry_widget):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, folder_selected)

# running the actual GUI
root = tk.Tk()
root.title("PySort")
root.geometry("650x275") # s ize of the window
root.iconbitmap('/Gui/icon.jpg')

main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# you always wanna start with the welcome screen, unless for testing purposes you can
# hardcode starting with one of the other ones.
welcome_screen(main_frame)

root.mainloop()