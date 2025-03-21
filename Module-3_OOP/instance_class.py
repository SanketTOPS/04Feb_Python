class studinfo:
    stid = 10
    stnm = "Sanket"

    def getdata(self):
        print("ID:", self.stid)
        print("Name:", self.stnm)


# Object of class
"""st = studinfo()
st.getdata()
st.stid = 12
st.stnm = "Nirav"
st.getdata()"""

# Instance
studinfo().getdata()
studinfo().stid = 45
studinfo().stnm = "Ashok"
studinfo().getdata()
