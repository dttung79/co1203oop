from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.__name = name
        self.__shape_type = 'General shape'
    
    @property
    def name(self):
        return self.__name
    
    @property
    def shape_type(self):
        return self.__shape_type
    
    @name.setter
    def name(self, name):
        self.__name = name

    @shape_type.setter
    def shape_type(self, shape_type):
        self.__shape_type = shape_type
    
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{self.__shape_type} {self.__name}, area: {self.area()}'