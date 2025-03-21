class master:
    # method overridinig
    def header(self, hid):
        print("This is header:", hid)

    def footer(self, fid):
        print("This is footer:", fid)


class home(master):
    def header(self, hid):
        return super().header(hid)

    def footer(self, fid):
        return super().footer(fid)


class about(master):
    def header(self, hid):
        return super().header(hid)

    def footer(self, fid):
        return super().footer(fid)
