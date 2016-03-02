import coffee2


class Coffee(object):
    def __init__(self, name):
        self.name = name

    def gettype(self):
        print(self.name)
        self.type = self.name.split(" ")[0:2]
        print("type: " + str(self.type))

    def getcountry(self):
        self.country = self.name.split(" ")[-2]
        print("country: " + str(self.country))

    def getrating(self):
        self.rating = self.name.split(" ")[-1]
        print("rating: " + str(self.rating))

def main():
    coffeeName1 = "Fair Trade Decaf Black Satin Panamanian " + str(coffee2.generaterating())
    coffee1 = Coffee(coffeeName1)
    coffee1.gettype()
    coffee1.getcountry()
    coffee1.getrating()

if __name__ == '__main__':
    main()
