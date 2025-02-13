no1 = int(input("Enter Number1:"))
no2 = int(input("Enter Number2:"))

print("1:Add")
print("2:Sub")
print("3:Mul")
print("4:Div")

n = int(input("Select any one option:"))

if n == 1:
    print("Add:", no1 + no2)
elif n == 2:
    print("Sub:", no1 - no2)
elif n == 3:
    print("Mul:", no1 * no2)
elif n == 4:
    print("Div:", no1 / no2)
else:
    print("Error!Invalid choice....")
