file = open("stdata.txt", "a")

n = int(input("Enter number of students:"))

for i in range(n):
    id = input("Enter an ID:")
    name = input("Enter a Name:")

    file.write(f"ID:{id}\nName:{name}\n")
