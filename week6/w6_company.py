from w6_employee import Employee
from w6_parttime import PartTime

class Company:
    def __init__(self, name):
        self.name = name
        self.__employees = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    def add(self, emp):
        self.__employees.append(emp)
    
    def remove(self, id):
        for emp in self.__employees:
            if emp.id == id:
                self.__employees.remove(emp)
                return 
        raise ValueError(f"Employee ID {id} not found")
    
    def raise_rate(self, id, new_rate):
        for emp in self.__employees:
            if emp.id == id:
                emp.rate += new_rate
                return
        raise ValueError(f"Employee ID {id} not found")
    
    def show_all(self):
        for emp in self.__employees:
            emp.show()
            print('----------------------')

if __name__ == '__main__':
    c = Company('ABC')
    c.add(Employee('John', 1000))
    c.add(PartTime('Jane', 20, 50))
    c.show_all()
    c.raise_rate(1, 100)
    c.show_all()
    c.remove(2)
    c.show_all()
    # c.remove(2) # error because ID 2 is not in the list (removed before)
    