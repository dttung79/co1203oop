# syntax to import: from file_name import class_name
from student import Student

class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = [] # a list of students, currently empty
    
    def add(self):
        id = int(input('Enter student id: '))
        name = input('Enter student name: ')
        math = float(input('Enter math grade: '))
        english = float(input('Enter english grade: '))
        literature = float(input('Enter literature grade: '))

        st = Student(id, name, math, english, literature)
        self.students.append(st) # add st to the list students
        print(f'Student id {id} added success.')
    
    def show_all(self):
        for st in self.students:
            st.show()
    
    def find_name(self):
        name = input('Enter name to search: ')
        found = False
        for st in self.students:
            if st.name.lower() == name.lower():
                st.show()
                found = True
        
        if not found:
            print(f'No student name {name}')
    
    def print_menu(self):
        print('1. Add student.')
        print('2. Show all.')
        print('3. Search by name.')
        print('0. Quit.')
    
    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = int(input('Your choice: '))
            if choice == 1: self.add()
            elif choice == 2: self.show_all()
            elif choice == 3: self.find_name()
            elif choice == 0: running = False


# Main
gch1203 = ClassRoom('GCH1203')
gch1203.run()