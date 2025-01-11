
class  Employee:
    file_path = "./python-homeworks/lesson-7/homework/employees.txt"
    
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def add_employee(self):
        with open(Employee.file_path, 'a') as f:
            data = f.write(f"{self.id}, {self.name}, {self.position}, {self.salary}\n")
        return f"{data}"

    def all_employees():
        with open(Employee.file_path, 'rt') as f:
            data = f.read()
        return data
    
    def search_employee(id):
        with open(Employee.file_path, 'rt') as f:
            data = f.readlines()
            employees = [list(val.split(',')) for val in data]
            for i in employees:
                if i[0] == str(id):
                    return i   

    def update_employee(id, name, position, salary):
        with open(Employee.file_path, 'r') as f:
            data = f.readlines()
        employees = [list(val.split(',')) for val in data]
        for employee in employees:
            if employee[0] == str(id):
                employee[1] = name
                employee[2] = position
                employee[3] = str(salary)
        with open(Employee.file_path, 'w') as f:
            for employ in employees:
                f.write(', '.join(employ) + '\n')
        with open(Employee.file_path) as f:
            infor = f.read()
        return infor

    def remove_employee(id):
        with open(Employee.file_path, 'rt') as f:
            data = f.readlines()
            employees = [list(val.split(',')) for val in data]
            for i in range(len(employees) - 1):
                if employees[int(i)][0] == str(id):
                    employees.pop(i)
        with open(Employee.file_path, 'w') as f:
            for employ in employees:
                f.write(', '.join(employ))
        with open(Employee.file_path) as f:
            infor = f.read()
        return infor


id = 1000  
while True:
    number = 0
    txt = int(input('''
        1. Add new employee record
        2. View all employee records
        3. Search for an employee by Employee ID
        4. Update an employee's information
        5. Delete an employee record
        6. Exit
'''))
    if txt == 1:
        employee = Employee(id, name=input('Ism kiriting: '), position=input('Lavozimingizni kiriting: '), salary=input('Maoshingizni kiriting: '))
        print(employee.add_employee())
        id += 1
    elif txt == 2:
        print(Employee.all_employees())
    elif txt == 3:
        print(Employee.search_employee(id=int(input('ID ni kiriting: '))))
    elif txt == 4:
        print(Employee.update_employee(id=int(input('ID ni kiriting: ')), name=input('Ism kiriting: '), position=input('Lavozimingizni kiriting: '), salary=input('Maoshingizni kiriting: ')))
    elif txt == 5:
        print(Employee.remove_employee(id=int(input('ID ni kiriting: '))))
    elif txt == 6:
        print('Goodbye')
        break
    else:
        print('Nimadir xato')
        number += 1