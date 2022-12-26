# Desktop-Organizer
Organizes your desktop into folders.
This code is a desktop organizer tool written in Python using the Tkinter library. When run, it creates a GUI window with a label and a button.

The main function of the code is to organize the files on the current user's desktop into separate folders based on their file type (as determined by the file extension). The code first creates a dictionary of file extensions and their corresponding folder names, then iterates through all of the files on the desktop. For each file, it gets the file extension and checks if it is in the file_types dictionary. If it is, the code gets the corresponding folder name and creates a new folder with that name if it doesn't already exist. The code then moves the file into the appropriate folder and updates the label to show the current file being moved.

Once all of the files have been processed, the label is updated to show that the organization is complete. The code also includes a "Undo" button that, when clicked, moves all of the files back to their original locations on the desktop and updates the label to show that the organization has been undone.

So far I have not been able to get the undo function to work, so take caution if your current desktop icon setup is something you care about when running this code.
