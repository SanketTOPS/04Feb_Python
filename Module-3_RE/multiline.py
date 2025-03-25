import re

mystr = "that is Python!"

# x = re.findall("^This", mystr)
# x = re.findall("^[A-Z]", mystr)
x = re.findall("on!$", mystr)
print(x)
