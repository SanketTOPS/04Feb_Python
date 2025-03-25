import re

mystr = "This is python!"

x = re.match("python", mystr)
print(x)

if x:
    print("Match success!")
else:
    print("Error!")
