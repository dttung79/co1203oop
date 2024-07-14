from w4_item import Item

class Store:
    def __init__(self, name):
        self.set_name(name)
        self.__items = []
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if name == '':
            print('Name cannot be empty')
            self.__name = 'No name'
        else:
            self.__name = name
    
    # don't provide get_items() method because it can expose the internal list
    
    def add(self, item):
        self.__items.append(item)
    
    def remove(self, name):
        item = self.__search(name)
        if not item:
            print(f'Item with name {name} not found')
            return
        self.__items.remove(item)

    def import_item(self, name, quantity):
        item = self.__search(name)
        if not item:
            print(f'Item with name {name} not found')
            return
        new_quantity = item.get_quantity() + quantity
        item.set_quantity(new_quantity)

    def export_item(self, name, quantity):
        item = self.__search(name)
        if not item:
            print(f'Item with name {name} not found')
            return
        new_quantity = item.get_quantity() - quantity
        if new_quantity < 0:
            print(f'Not enough {name} in stock')
            return
        item.set_quantity(new_quantity)

    def __search(self, name):
        for item in self.__items:
            if item.get_name() == name:
                return item
        return None
    
    def find_max_total(self):
        if len(self.__items) == 0:
            print('No item in store')
            return
        
        max_total = 0
        max_item = None
        for item in self.__items:
            if item.get_total_value() > max_total:
                max_total = item.get_total_value()
                max_item = item
        print('Item with max total value:')
        max_item.show_info()

    def show_all(self):
        for item in self.__items:
            item.show_info()