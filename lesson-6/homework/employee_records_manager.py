file_path = "./python-homeworks/lesson-6/homework/employees.txt"

def add_employee(id, name, position, salary):
    with open(file_path, 'a') as f:
        data = f.write(f"{id}, {name}, {position}, {salary}\n")
    return f"Qo'shildi"
# print(add_employee(1001, 'John Doe', 'Software Engineer', 75000))
# print(add_employee(1002, 'Tom Adamson', 'Project Manager', 80000))

def all_employees():
    with open(file_path, 'rt') as f:
        data = f.read()
    return data
# print(all_employee())

def search_employee(id):
    with open(file_path, 'rt') as f:
        data = f.readlines()
        employees = [list(val.split(',')) for val in data]
        for i in employees:
            if i[0] == str(id):
                return i   
# print(search_employee(1001))

def update_employee(id, name, position, salary):
    with open(file_path, 'r') as f:
        data = f.readlines()
    employees = [list(val.split(',')) for val in data]
    for employee in employees:
        if employee[0] == str(id):
            employee[1] = name
            employee[2] = position
            employee[3] = str(salary)
    with open(file_path, 'w') as f:
        for employ in employees:
            f.write(', '.join(employ) + '\n')
    with open(file_path) as f:
        infor = f.read()
    return infor
# print(update_employee(1001, 'Zafar Kho', 'Senior Developer', 20000))

def remove_employee(id):
    with open(file_path, 'rt') as f:
        data = f.readlines()
        employees = [list(val.split(',')) for val in data]
        for i in range(len(employees) - 1):
            if employees[int(i)][0] == str(id):
                employees.pop(i)
    with open(file_path, 'w') as f:
        for employ in employees:
            f.write(', '.join(employ))
    with open(file_path) as f:
        infor = f.read()
    return infor
# print(remove_employee(1001))

    
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
        print(add_employee(id, name=input('Ism kiriting: '), position=input('Lavozimingizni kiriting: '), salary=input('Maoshingizni kiriting: ')))
        id += 1
    elif txt == 2:
        print(all_employees())
    elif txt == 3:
        print(search_employee(id=int(input('ID ni kiriting: '))))
    elif txt == 4:
        print(update_employee(id=int(input('ID ni kiriting: ')), name=input('Ism kiriting: '), position=input('Lavozimingizni kiriting: '), salary=input('Maoshingizni kiriting: ')))
    elif txt == 5:
        print(remove_employee(id=int(input('ID ni kiriting: '))))
    elif txt == 6:
        break
    else:
        print('Nimadir xato')
        number += 1