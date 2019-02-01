#!/usr/bin/env python

import sys
import os


def create_3_file(file_name_3):
    dir_name = 'new_defconfig'
    name_file_save = os.path.join(dir_name, str(file_name_3))
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    f = open(name_file_save, 'w')
    f.close()
    return name_file_save


def save_for_3_file(opened_file, file_name, mark_search):
    with open(file_name, 'a') as f:
        while True:
            data = opened_file.readline()
            f.write(data)
            if mark_search in data or not data:
                break


def open_read_1_file(file_name_1, file_name_3):
    with open(file_name_1, 'r') as f:
        mark = "# Kernel Configuration"
        save_for_3_file(f, file_name_3, mark)
    with open(file_name_3, 'a') as f:
        data = '#\n'
        f.write(data)


def open_read_2_file(file_name_2, file_name_3):
    with open(file_name_2, 'r') as f:
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        save_for_3_file(f, file_name_3, mark_search
            ='@')
    with open(file_name_3, 'a') as f:
        data = '#\n# End of Kernel Configuration\n#\n'
        f.write(data)



if __name__ == '__main__':
    name_1 = sys.argv[1]
    name_2 = sys.argv[2]
    name_3 = sys.argv[3]
    name_3 = create_3_file(name_3)
    open_read_1_file(name_1, name_3)
    open_read_2_file(name_2, name_3)