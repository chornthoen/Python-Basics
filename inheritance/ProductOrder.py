
class Product1:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def toString(self):

        return self.name + "," + str(self.year)


class OrderProduct(Product1):

    def __init__(self, name, year, code, qty, price):
        super().__init__(name, year)
        self.code = code
        self.qty = qty
        self.price = price

    def getPrice(self):
        return self.qty * self.price

    def toString(self):
        return super().toString() + "," + str(self.code) + \
               "," + str(self.qty) + "," + str(self.price) + "," + str(self.getPrice())

    def disPlay(self):
        print("Name =", self.name, ",Year =", self.year, ",Code =", self.code,
              ",Qty =", self.qty, ",Price =", self.price, ",Total =", self.getPrice())


order = OrderProduct("Computer", 2022, 101, 2, 2000)
print("to String .....")
print(order.toString())
order.disPlay()
