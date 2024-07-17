class Employee:
    auto_id = 0
    def __init__(self, name, rate):
        self.__id = Employee.auto_id
        Employee.auto_id += 1

        self.name = name
        self.rate = rate
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def rate(self):
        return self.__rate
    
    @name.setter
    def name(self, name):
        self.__name = name

    @rate.setter
    def rate(self, rate):
        self.__rate = rate

    def show(self):
        print(f'ID: {self.id}, Name: {self.name}, Salaray: ${self.salary()}')
    
    def salary(self):
        return self.rate * 800

if __name__ == '__main__':
    e1 = Employee('Alice', 1)
    e2 = Employee('Bob', 2)
    e3 = Employee('Charlie', 2.5)
    e1.show()
    e2.show()
    e3.show()
