s1 = int(input("Enter Subject1 Mark:"))
s2 = int(input("Enter Subject2 Mark:"))
s3 = int(input("Enter Subject3 Mark:"))
s4 = int(input("Enter Subject4 Mark:"))

if s1 >= 40 and s2 >= 40 and s3 >= 40 and s4 >= 40:  # ROOT - Parent
    total = s1 + s2 + s3 + s4
    print("Total:", total)

    pr = total / 4
    print("PR:", pr)

    if pr >= 70:  # Child
        print("Result:A+ or Dist.")
    elif pr >= 60:  # Child
        print("Result:A or First Class")
    elif pr >= 50:
        print("Result:B or Second Class")
    elif pr >= 40:  # Child
        print("Result:C or Pass Class")

else:
    print("Result:FAIL")
