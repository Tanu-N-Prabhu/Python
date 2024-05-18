"""
Rocky is creating his own operating system called “myFirst OS.” 
It’s a GUI-based OS where everything is stored in files and folders.
Rocky faces issues with creating unique folder names. If a folder name already exists, 
an integer is added to make it unique (starting from 1 and incrementing for each new request).
Given a list of folder names, process all requests and return an array of corresponding folder names.

Example:
Input: [“folder”, “folder”, “folder”, “folder”, “folder”]
Output: [“folder”, “folder1”, “folder2”, “folder3”, “folder4”]
"""


def unique_folder_names(folder_names):
    # Dictionary to store the count of each folder name encountered
    unique_folders = {}
    # Result list to store the final folder names
    result = []

    # Iterate through each folder name
    for folder in folder_names:
        # If the folder name is not encountered before, add it to the result list
        if folder not in unique_folders:
            unique_folders[folder] = 0
            result.append(folder)
        else:
            # If the folder name is encountered before, increment the count and append an integer
            unique_folders[folder] += 1

            # otherwise folder name should be with the number of this folder name
            new_folder = folder + str(unique_folders[folder])
            result.append(new_folder)

    # Return the array of corresponding folder names
    return result


# Example usage:
folder_names = ["folder", "folder", "folder", "folder", "folder"]
# Output: ["folder", "folder1", "folder2", "folder3", "folder4"]
print(unique_folder_names(folder_names))
