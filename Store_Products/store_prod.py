class Store:
    def __init__(self, name):
        self.name = name
        self.list = []
    def add_product(self, new_product):
        self.list.append(new_product)
        return self
    # def find_index(self, prod):
    #     count = 0
    #     for t in self.list:
    #         count += 1
    #         if t.name == prod:
    #             print(f'{prod} is at location {count}')
    def sell_product(self, prod):
        # print(self.list[id])
        count = -1
        for t in self.list:
            count += 1
            if t.name == prod:
                print(f'{prod} is at location {count}')
                self.list.remove(self.list[count])
                print(f'{prod} is now removed from your list')
                self.see_list()
        return self
    def inflation(self, percent_increase):
        for i in self.list:
            i.update_price(percent_increase, is_increased=True)
    def see_list(self):
        temp_list = []
        for item in self.list:
            temp_list.append(item.name)
        print(f'Here is your current list of products: {temp_list}')
    

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += round(self.price*percent_change, 2)
        else:
            self.price -= round(self.price*percent_change, 2)
        self.print_info()
        return self
    def print_info(self):
        print(f'Product Name: {self.name}, Category: {self.category}, Price: {self.price}')
        return self

# Create instance of Product class
p = Product('banana', 1.50, 'fruit')

# Call function in Product class printing Instance Info
p.print_info()

# Create instance of Store class
s = Store('Safeway')

# Call function in Product class that updates price and prints new info
p.update_price(0.25, True)

# Call function in Store class that adds instance of Product class to list 
s.add_product(p)

# Print list to verify it worked
s.see_list()

# Create 4 more instances of Product class 
q = Product('milk', 3.99, 'dairy')
r = Product('eggs', 7.99, 'dairy')
d = Product('soda', 3.50, 'drink')
m = Product('mushrooms', 7.56, 'produce')

# Call function in Store class that adds all new instances of Product class to list
s.add_product(q).add_product(r).add_product(d).add_product(m)

# Print list to verify it worked
s.see_list()

# Call function in Product class that updates price and prints new info
p.update_price(0.2, True)

# Call function that sells the product and removes it from the Store list
s.sell_product('soda')

# Call function that increases all prices
s.inflation(0.15)

s.see_list()
# print(p.__dict__)
