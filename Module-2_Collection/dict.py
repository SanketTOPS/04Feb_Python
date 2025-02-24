stdata = {"id": 101, "name": "Sanket", "city": "Rajkot"}

"""print(stdata)
print(stdata["name"])
print(stdata.get("city"))"""

"""print(stdata.keys())
print(stdata.values())
print(len(stdata))"""

# -------------------------------- #
# print(stdata)

"""for i in stdata:
    print(i)"""


"""for i in stdata.values():
    print(i)"""


"""for i in stdata.items():
    print(i)"""

"""for i, j in stdata.items():
    # print(i, j)
    print(f"Key={i}, Value={j}")"""

"""if "name" in stdata:
    print("Yes...")
else:
    print("Noo...")"""


"""if "Sanket" in stdata.values():
    print("Yes...")
else:
    print("Noo...")"""


# ---------------------------------- #
print(stdata)

stdata["id"] = 102
stdata["sub"] = "Python"
stdata.pop("city")
stdata.clear()
print(stdata)
