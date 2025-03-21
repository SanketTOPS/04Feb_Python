class studinfo:
    # method overloading
    def getdata(self, id):
        print("ID:", id)

    def getdata(self, name):
        print("Name:", name)


st = studinfo()
st.getdata(101)
st.getdata("Sanket")
