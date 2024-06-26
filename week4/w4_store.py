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