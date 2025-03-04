def add(a, b):
    print("Sum:", a + b)


def sub(a, b):
    print("Sub:", a + b)


def mul(a, b):
    print("Mul:", a + b)


def div(a, b):
    print("Div:", a + b)


while True:
    n = int(input("Enter your choice:"))
    if n == 1:
        add(23, 56)
    elif n == 2:
        sub(34, 6)
    elif n == 3:
        mul(12, 45)
    elif n == 4:
        div(34, 67)
    else:
        print("Error!Invalid choice...")
   
    ch = input("Do you want to continue? :")
    if ch == "y" or "Y":
        
    else:
        print("Bye...")
