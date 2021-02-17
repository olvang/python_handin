import argparse
import csv

parser = argparse.ArgumentParser(
    description='A Program to read a csv, and also some file writing')
parser.add_argument('path', help='csv file path to read')
parser.add_argument(
    '--file', help='The output destination file')


def print_file_content(file):
    with open(file) as file_object:
        contents = file_object.read()
        print(contents)


def write_list_to_file(output_file, *strings):
    with open(output_file, 'a') as file_object:
        for string in strings:
            file_object.write(string[0] + '\n')


def read_csv(input_file, output_file):
    with open(input_file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        if len(output_file) == 0:
            print(data)
        else:
            for string in data:
                write_list_to_file(output_file, string)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.file:
        output_file = args.file
    else:
        output_file = ''
    read_csv(args.path, output_file)
