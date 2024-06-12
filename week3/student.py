class Student:
    def __init__(self, id, name, math, english, literature):
        self.id = id
        self.name = name
        self.math = math
        self.english = english
        self.literature = literature
    
    def show(self):
        print(f'ID: {self.id}, name: {self.name}, GPA: {self.gpa():.2f}')
    
    def gpa(self):
        return (self.math + self.english + self.literature) / 3