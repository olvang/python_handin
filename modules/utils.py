import os


def get_file_names(folderpath, out='output.txt'):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(folderpath):
        f.extend(filenames)
        break
    with open(out, 'a') as file_object:
        for file in f:
            file_object.write(file + '\n')


def get_all_file_names(folderpath):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(folderpath):
        f.extend(filenames)
    print(f)


def print_line_one(*file_names):
    for filename in file_names:
        with open(filename) as f:
            first_line = f.readline()
            print(first_line)


def print_emails(*file_names):
    for filename in file_names:
        myfile = open(filename, 'r')
        for line in myfile:
            if "@" in line:
                print(line)


def write_headlines(*md_files, out='output_md.txt'):
    with open(out, 'a') as file_object:
        for md_file in md_files:
            myfile = open(md_file, 'r')
            for line in myfile:
                if line.startswith('#'):
                    file_object.write(line + '\n')
