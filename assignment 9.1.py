# Write a Python program to do everything the file command can do

import magic
import argparse
import os

def file_command():
    parser = argparse.ArgumentParser(description='Determine file type')
    parser.add_argument('files', nargs='+')
    args = parser.parse_args()

    try:
        for file in args.files:
            if os.path.isdir(file):
                print(f'{file}: directory')
            else:
                print(f'{file}: {magic.from_file(file)}')
    except: print('Not a good file')

if __name__ == '__main__':
    file_command()