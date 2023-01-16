import os
import tkinter as tk
from tkinter import filedialog


def select_directory():
    # open a file dialog and get the selected directory
    directory = filedialog.askdirectory()
    # print the selected directory
    return directory


# create a tkinter window
root = tk.Tk()
root.title("Select Directory")
root.geometry("300x300")

# create a button to open the file dialog
button = tk.Button(root, text="Select Directory", command=select_directory)
button.pack()

# start the tkinter event loop
root.mainloop()


def list_files(directory):
    # create an empty list to store the files
    files = []
    # use the os.listdir() method to get a list of all files and directories in the given directory
    for file_name in os.listdir(directory):
        files.append(file_name)
    # return the list of files
    return files


# example usage
files = list_files(select_directory)

for i in files:
    print(i)
