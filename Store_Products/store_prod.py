class Store:
    def __init__(self, name):
        self.name = name
        self.list = []
    def add_product(self, new_product):
        self.new_product = new_product
        self.list.append(self.new_product)
        return self
    def sell_product(self, id):
        self.id = id
        self.list.remove(self.list[id])
        return self
    def inflation(self, percent_increase):
        self.percent_increase = percent_increase
        Product.update_price(self.percent_increase, is_increased=True)
    

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        self.percent_change = percent_change
        self.is_increased = is_increased
        if is_increased == True:
            self.price += self.price*percent_change
        else:
            self.price -= self.price*percent_change
        self.print_info()
        return self
    def print_info(self):
        print(f'Product Name: {self.name}, Category: {self.category}, Price: {self.price}')
        return self


p = Product('banana',1.50, 'fruit')
p.print_info()
s = Store('Safeway')
s.add_product(p.name)
p.update_price(0.25, True)
q = Product('milk', 3.99, 'dairy')
r = Product('eggs', 7.99, 'dairy')
d = Product('soda', 3.50, 'drink')
m = Product('mushrooms', 7.56, 'produce')
print(s.list)
s.add_product(q.name).add_product(r.name).add_product(d.name).add_product(m.name)
print(s.list)
print(s.list[2])
s.sell_product(2)
print(s.list)
# s.inflation(0.5)
