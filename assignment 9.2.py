#Write a Python program to do everything the cut command can do

import argparse
from ast import arg
import sys

def list_data_of_file():
    for element in args.bytes:
        if element.endswith('.txt'):
            with open(element, 'r') as f:
                list_data = f.read().split('\n')
    return list_data

def select_by_bytes(list_data):
    choice = str(args.bytes[0]).split(',')
    for data in list_data:
        respone = ''
        for i in choice:
            respone += data[int(i)-1]
        print(respone)

def select_range(list_data, index):
    for data in list_data:
        respone=''
        for i in index:
            respone += data[int(i[0]) -1 : int(i[1]) -1]
        print(respone)


parser = argparse.ArgumentParser(description='Remove sections from each line of files')
parser.add_argument('-b', '--bytes', nargs='*' ,help='select only these bytes')
parser.add_argument('--version',action='version', version=sys.version, help='output version information and exit')
args = parser.parse_args()

if not any(vars(args).values()):# check arguments required
    parser.error('No arguments provided.')

if args.bytes != None:
    flag = 0
    index = []
    try:
        if len(args.bytes) < 2:
            print("input wrong!")
        else:
            for element in args.bytes:
                if  "-" in element: # input range
                    flag = 1
            if flag == 1:
                index.append(str(element).split('-'))
                select_range(list_data_of_file(), index)
            
            if flag == 0: #input bytes
                select_by_bytes(list_data_of_file())

    except(FileNotFoundError):
        print('File not found')
    except IndexError:
        print('Input out of range of text')
    except ValueError:
        print('Input range or number of bytes')

 

    




        
        
