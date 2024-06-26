class Item:
    def __init__(self, name, price, quantity):
        self.set_name(name)
        self.set_price(price)
        self.set_quantity(quantity)

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
    
    def set_name(self, name):
        if name == '':
            print('Name cannot be empty')
            self.__name = 'No name'
        else: 
            self.__name = name
    
    def set_price(self, price):
        if price < 0:
            print('Price cannot be negative')
            self.__price = 0
        else:
            self.__price = price

    def set_quantity(self, quantity):
        if quantity < 0:
            print('Quantity cannot be negative')
            self.__quantity = 0
        else:
            self.__quantity = quantity
    
    def show_info(self):
        print(f'Item {self.__name}, ${self.__price} x {self.__quantity} = ${self.get_total_value()}')
    
    def get_total_value(self):
        return self.__price * self.__quantity

## test
# computer = Item('Computer', 1000, 5)
# computer.show_info()
# computer.set_name('')
# computer.set_price(-100)
# computer.set_quantity(-5)
# computer.show_info()