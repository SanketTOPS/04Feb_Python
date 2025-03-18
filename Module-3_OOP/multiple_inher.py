class python:
    pid: int
    p_name: str

    def p_getdata(self):
        self.pid = input("Enter Python's ID:")
        self.p_name = input("Enter Python's Name:")


class java:
    jid: int
    j_name: str

    def j_getdata(self):
        self.jid = input("Enter Java's ID:")
        self.j_name = input("Enter Java's Name:")


class html:
    hid: int
    h_name: str

    def h_getdata(self):
        self.hid = input("Enter HTML's ID:")
        self.h_name = input("Enter HTML's Name:")


class tops(python, java, html):
    def printdata(self):
        print("---------Python's Data--------")
        print("Python's ID:", self.pid)
        print("Python's Name:", self.p_name)
        print("---------JAVA's Data--------")
        print("JAVA's ID:", self.jid)
        print("JAVA's Name:", self.j_name)
        print("---------HTML's Data--------")
        print("HTML's ID:", self.hid)
        print("HTML's Name:", self.h_name)


tp = tops()
tp.p_getdata()
tp.j_getdata()
tp.h_getdata()
tp.printdata()
