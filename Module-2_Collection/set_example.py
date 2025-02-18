data = {"a", "b", "c", "d", "e", "a"}
# print(data)
# print(data[0])
# print(len(data))

"""if "b" in data:
    print("Yes...")
else:
    print("Noo")"""

# -------------------------------- #

"""for i in data:
    print(i)"""

# -------------------------------- #
# Set Methods
"""print(data)
data.add("f")
data.update(["g", "h", "i"])
data.remove("c")
data.clear()
#del data
print(data)"""

# ---------------------------- #
newdata = {"x", "y", "z", "a", "b"}
print(data)
print(newdata)

# x = data.union(newdata)
x = data.intersection(newdata)
print(x)
