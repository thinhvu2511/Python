# Given a folder that contains some file that has a character of a flag and others do not. Find the flag

import os
import re

path = './find_the_flag'

lst = os.listdir(path)
for file in lst:
    a = os.path.join(path, file) # Nối đường dẫn path với file
    if os.path.isfile(a):
        f = open(a)
        check = f.read() # Đọc file
        if not re.match(r"^\d(\d|Not).*", check):
            print('This file: '+ check)

        