stdata = []


n = int(input("Enter number of students:"))

for i in range(n):
    data = {}
    id = input("Enter an ID:")
    nm = input("Enter a Name:")
    ct = input("Enter a City:")
    data["id"] = id
    data["name"] = nm
    data["city"] = ct

    stdata.append(data)

print(stdata)
