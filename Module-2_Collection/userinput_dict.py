"""stdata = {}

n = int(input("Enter number of pairs:"))

for i in range(n):
    k = input("Enter your Key's:")
    v = input("Enter your Value's:")
    stdata[k] = v


print(stdata)
"""

# ------------------------------ #

stdata = {}

keys = ["id", "name", "city"]

for i in range(len(keys)):
    v = input(f"Enter your Value's for {keys[i]}:")
    stdata[keys[i]] = v


print(stdata)
