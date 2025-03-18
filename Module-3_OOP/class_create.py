class studinfo:
    stid = 12
    stnm = "Sanket"

    def myfunc(self):
        print("This is OOP in Python!")

    def getsum(self, a, b):
        print("Sum:", a + b)


# Object of class
st = studinfo()
print("ID:", st.stid)
print("Name:", st.stnm)
st.myfunc()
st.getsum(12, 56)
