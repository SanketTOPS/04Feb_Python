stdata = {"id": 101, "name": "sanket", "city": "rajkot"}

"""print(stdata)
print(stdata["name"])
print(stdata.get("city"))
print(stdata.keys())
print(stdata.values())
print(len(stdata))
stdata["id"] = 102
print(stdata)"""

# ----------------------------------------- #

# print(stdata)

"""if "name" in stdata:
    print("Yes...")
else:
    print("No")"""

"""if "sanket" in stdata.values():
    print("Yes...")
else:
    print("No")"""

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""


"""for i, j in stdata.items():
    # print(i, j)
    print(f"Key={i} and Value={j}")"""


# ----------------------------------------- #


print(stdata)
stdata["sub"] = "Python"  # Add
stdata["name"] = "Ashok"  # Update
stdata.pop("city")
# stdata.clear()
# del stdata
print(stdata)
