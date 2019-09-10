class Honda:
    def sedan(self):
        print("Honda City")

class Maruti:
    def sedan(self):
        print("Ciaz")

class ShowRoom:
    def car(self,company):
        company.sedan()

sr = ShowRoom()
mr = Maruti()
hd = Honda()
sr.car(hd)
sr.car(mr)
