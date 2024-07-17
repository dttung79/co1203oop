from w6_employee import Employee

class PartTime(Employee):
    def __init__(self, name, rate, days):
        super().__init__(name, rate)    # call constructor of parent class to set name and rate
        self.days = days
    
    @property
    def days(self):
        return self.__days
    
    @days.setter
    def days(self, days):
        self.__days = days

    def show(self):
        super().show()
        print(f'Work Days: {self.days}')

    def salary(self):
        return super().salary() * self.days / 5

if __name__ == '__main__':
    e1 = Employee('Alice', 1)
    e2 = PartTime('Bob', 2, 3)
    e3 = Employee('Charlie', 2.5)
    e4 = PartTime('David', 3, 4)

    e1.show()
    e2.show()
    e3.show()
    e4.show()