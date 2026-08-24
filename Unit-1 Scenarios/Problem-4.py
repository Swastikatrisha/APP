class Mobile():
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
class Standard(Mobile):
    def __init__(self, brand, model, price,premium,mid,budget):
        super().__init__(brand, model, price)
        self.premium=premium
        self.mid=mid
        self.budget=budget

class Store():
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_all(self):
        for mobile in self.mobiles:
            print("Brand:", mobile.brand)
            print("Model:", mobile.model)
            print("Price:", mobile.price)

store = Store()

m1 = Standard("Apple", "iPhone 15", 60000, "Premium", "Mid-range", "Budget")
m2 = Standard("Samsung", "A55", 35000, "Premium", "Mid-range", "Budget")
m3 = Standard("Redmi", "Note 13", 15000, "Premium", "Mid-range", "Budget")

store.add_mobile(m1)
store.add_mobile(m2)
store.add_mobile(m3)

store.display_all()
