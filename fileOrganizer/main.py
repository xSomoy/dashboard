import os

def list_files(directory):
    # create an empty list to store the files
    files = []
    # use the os.listdir() method to get a list of all files and directories in the given directory
    for file_name in os.listdir(directory):
        # use the os.path.join() method to construct the full file path
        #file_path = os.path.join(directory, file_name)
        # check if the file is a regular file (not a directory)
        #if os.path.isfile(file_path):
            # add the file to the list
            files.append(file_name)
    # return the list of files
    return files

# example usage
files = list_files("D:\\Downloads")

for i in files:
    print(i)
