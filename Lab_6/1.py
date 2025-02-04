import os

def list_directories_and_files(path):
    directories = []
    files = []

    items = os.listdir(path)
    
    for item in items:
        item_path = path + '/' + item
        
        if os.path.isdir(item_path):
            directories.append(item)
        else:
            files.append(item)
    
    return directories, files

path = "/Users/talanterzhan/Documents/GitHub/pp_2/Lab_6"

directories, files = list_directories_and_files(path)

print("Directories:")
for directory in directories:
    print(directory)

print("\nFiles:")
for file in files:
    print(file)

#---------------------------Task--------------------------


def check_path_access(path):
    access_info = {}
    access_info['exists'] = os.path.exists(path)
    access_info['readable'] = os.access(path, os.R_OK)
    access_info['writable'] = os.access(path, os.W_OK)
    access_info['executable'] = os.access(path, os.X_OK)
    return access_info

access_info = check_path_access(path)

print(f"Path: {path}")
print(f"Exists: {access_info['exists']}")
print(f"Readable: {access_info['readable']}")
print(f"Writable: {access_info['writable']}")
print(f"Executable: {access_info['executable']}")

#---------------------------Task--------------------------
def check_path(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        return True, directory, filename
    else:
        return False, None, None

exists, directory, filename = check_path(path)

if exists:
    print("Path exists.")
    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("Path does not exist.")

#---------------------------Task--------------------------
def count_lines(filename):
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count

filename = "words.txt"
num_lines =count_lines(filename)
if num_lines > 0:
    print(num_lines)

#---------------------------Task--------------------------

def get_content_lines(filename):
        with open(filename, 'r') as file:
            for line in file:
                yield line
def write_list_to_file(filename, my_list):
        with open(filename, 'w') as file:
            for item in my_list:
                file.write(str(item))

my_list = get_content_lines(filename)
filename = "output.txt"  
write_list_to_file(filename, my_list)

#---------------------------Task--------------------------

import string

def generate_files():
    letters = string.ascii_uppercase

    for letter in letters:
        filename = f"Hello World/{letter}.txt"
        if(path.exists(filename)):
            filename = f"Hello World/{letter}./{letter}.txt"
        with open(filename, 'w') as file:
            file.write(filename)

generate_files()

#---------------------------Task--------------------------

def delete_file(path):
    letters = string.ascii_uppercase
    for letter in letters:
         new_path = os.path.join(path, letter+".txt")
         if os.path.exists(new_path):
            os.remove(new_path)
         else:
            print(f" File '{new_path}' do not exist.")

file_path = "/Users/talanterzhan/Documents/GitHub/pp_2/Lab_6/Hello World"

access_info = delete_file(file_path)

