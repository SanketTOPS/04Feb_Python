import re

mystr = "This is python!"

x = re.findall("is", mystr)
print(x)

if x:
    print("Match success!")
else:
    print("Error!")
