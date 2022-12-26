import os
import shutil
import getpass
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Desktop Organizer")

# Create a label to display the progress
label = tk.Label(root, text="Organizing files...")
label.pack()

# Get the current user's username
username = getpass.getuser()

# Set the path to your desktop using the retrieved username
desktop_path = f"C:\\Users\\{username}\\Desktop"

# Create a list of file extensions and their corresponding folder names
file_types = {
    ".exe": "Programs",
    ".docx": "Documents",
    ".jpg": "Images",
    ".mp3": "Music",
    ".txt": "Text Files",
    ".pdf": "PDF Files",
    ".zip": "Archives",
    ".xlsx": "Excel Files",
    ".pptx": "PowerPoint Files",
    ".mp4": "Videos",
    ".png": "PNG Images",
    ".gif": "GIF Images",
    ".bmp": "BMP Images",
    ".avi": "AVI Videos",
    ".wmv": "WMV Videos",
    ".mov": "MOV Videos",
    ".flv": "FLV Videos",
    ".psd": "Photoshop Files",
    ".html": "HTML Files",
    ".css": "CSS Files"
}

# Create a dictionary to store the created folders
folders = {}

# Create a dictionary to store the original file locations
original_locations = {}

def undo():
    # Iterate through the dictionary of original file locations
    for filename, original_location in original_locations.items():
        # Move the file back to its original location
        shutil.move(os.path.join(desktop_path, filename), original_location)
    # Update the label text to show that the organization has been undone
    label.config(text="Desktop organization undone!")

# Iterate through all of the files on the desktop
for filename in os.listdir(desktop_path):
    # Get the file extension of the current file
    extension = os.path.splitext(filename)[1]
    # If the file extension is in the file_types list
    if extension in file_types:
        # Get the corresponding folder name
        folder_name = file_types[extension]
        # If the folder has not yet been created
        if folder_name not in folders:
            # Create the folder
            os.mkdir(os.path.join(desktop_path, folder_name))
            # Add the folder to the dictionary
            folders[folder_name] = True
        # Store the original location of the file in the dictionary
        original_locations[filename] = os.path.join(desktop_path, filename)
        # Move the file into the appropriate folder
        shutil.move(os.path.join(desktop_path, filename), os.path.join(desktop_path, folder_name))
        # Update the label text to show the current file being moved
        label.config(text=f"Moving {filename} to {folder_name}")
        # Update the GUI
        root.update()

# Update the label text to show that the organization is complete
label.config(text="Desktop organization complete!")

# Create a button to undo the organization
undo_button = tk.Button(root, text="Undo", command=undo)
undo_button.pack()

# Run the main loop
root.mainloop()