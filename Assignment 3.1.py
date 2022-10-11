# You and Fredrick are good friends. YesterAssignment, Fredrick received credit cards from ABCD Bank. 
# He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

# A valid credit card from ABCD Bank has the following characteristics:
# ► It must start with a 4, 5 or 6.
# ► It must contain exactly 16 digits.
# ► It must only consist of digits (0-9).
# ► It may have digits in groups of 4, separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have 4 or more consecutive repeated digits.

import re

def CheckCardNum(num):
	if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", num) and not re.search(r"-*([\d])\1{3}", '-'.join(num.replace("-", "")[i:i+4] for i in range(0, len(num.replace("-", "")), 4))):
		print('Valid')
	else: 
        	print('Invalid')

num = input('Input Credit Card Number: ')
CheckCardNum(num)
