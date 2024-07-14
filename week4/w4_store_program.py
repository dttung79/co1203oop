from w4_item import Item
from w4_store import Store

class StoreProgram:
    def __init__(self, name):
        self.__store = Store(name)
    
    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1:     self.__add_item()
            elif choice == 2:   self.__remove_item()
            elif choice == 3:   self.__import_item()
            elif choice == 4:   self.__export_item()
            elif choice == 5:   self.__find_max_item()
            elif choice == 6:   self.__show_all()
            elif choice == 0:   running = False
            else:               print('Invalid choice!')
    
    def __print_menu(self):
        print('1. Add item')
        print('2. Remove item')
        print('3. Import item')
        print('4. Export item')
        print('5. Find max item')
        print('6. Show all items')
        print('0. Exit')
    
    def __add_item(self):
        name = input('Enter item name: ')
        price = float(input('Enter item price: '))
        quantity = int(input('Enter item quantity: '))
        item = Item(name, price, quantity)
        self.__store.add(item)
        print(f'Item {name} added successfully')

    def __remove_item(self):
        name = input('Enter item name to remove: ')
        self.__store.remove(name)
    
    def __import_item(self):
        name = input('Enter item name to import: ')
        quantity = int(input('Enter quantity to import: '))
        self.__store.import_item(name, quantity)
    
    def __export_item(self):
        name = input('Enter item name to export: ')
        quantity = int(input('Enter quantity to export: '))
        self.__store.export_item(name, quantity)

    def __find_max_item(self):
        self.__store.find_max_total()

    def __show_all(self):
        self.__store.show_all()

### Main Program ###
program = StoreProgram('ABC')
program.run()