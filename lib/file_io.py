import os

def write_file(file_name, file_content):
    full_path = os.path.join('/home/dongkuei/Desktop/flatIron/phase03/python-p3-fileio-lab/lib/', f'{file_name}.txt')
    with open(full_path, mode='w', encoding='utf-8') as file_obj:
        file_obj.write(file_content)


def append_file(file_name, append_content):
    full_path = os.path.join('/home/dongkuei/Desktop/flatIron/phase03/python-p3-fileio-lab/lib/', f'{file_name}.txt')
    with open(full_path, mode='a', encoding='utf-8') as file_obj:
        file_obj.write(append_content)

import os

def read_file(file_name):
    full_path = os.path.join('/home/dongkuei/Desktop/flatIron/phase03/python-p3-fileio-lab/lib/', f'{file_name}.txt')
    with open(full_path, encoding='utf-8') as file_obj:
        content = file_obj.read()  # Read the entire content of the file
    return content
