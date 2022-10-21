# Get the flag from this text
# The progress to get this text:
# Base64 -> Rot113 -> Decimal -> Hex -> Binary -> Base64

import base64
import codecs

# we need to go against from Base64 -> Rot113 -> Decimal -> Hex -> Binary -> Base64

text_flag = 'MDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMTAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDEwMDAxMTAwMTEwMDExMDAwMDAwMTEwMDExMDAxMTAxMDAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMTAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMDExMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMTExMDAxMTAwMTEwMDExMDExMDAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAxMTAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMTExMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDEwMDAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMDExMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDAwMDAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAxMTAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMTAxMDAxMTAwMTEwMDExMDExMQ=='

text_flag = base64.b64decode(text_flag) # decode base64 and get binary
text_flag = text_flag.decode('ascii') 
text_flag = hex(int(text_flag, 2)) # convert binary to hex
text_flag = codecs.decode(text_flag[2:], 'hex') # decode hex to text 
text_flag = codecs.decode(text_flag, 'hex')
text_flag = text_flag.decode('ascii')

text_bytes_array = []
i = 0
while i < len(text_flag): # the array with list decimal number
    if text_flag[i] == '1':
        text_bytes_array.append(text_flag[i:i+3])
        i += 3
    else:
        text_bytes_array.append(text_flag[i:i+2])
        i += 2
        
text_flag = ''

for ch in text_bytes_array: # Convert to ascii
    text_flag += chr(int(ch))

text_flag = codecs.encode(text_flag, 'rot_13') # encode rot13
text_flag = base64.b64decode(text_flag)
text_flag = text_flag.decode('ascii')
print(text_flag)


