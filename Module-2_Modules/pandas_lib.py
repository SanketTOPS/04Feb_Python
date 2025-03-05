import pandas

# x = pandas.read_csv("demo.csv")
# print(x)

stdata = {
    "ID": [1, 2, 3],
    "Name": ["Sanket", "Hitesh", "Ashok"],
    "City": ["Rajkot", "Baroda", "Surat"],
}

# print(stdata)
x = pandas.DataFrame(stdata)
print(x)
