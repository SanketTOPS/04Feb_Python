a = 10
print("A:", a)


def getvalue():
    global a
    a += 1
    print("A:", a)


getvalue()
