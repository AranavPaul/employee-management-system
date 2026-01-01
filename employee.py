import random

def add_employee(name):
    employees = get_employee() #We created datatype because txt files don't understand python objects
    id = random.randint(100000000, 999999999)
    employees[id] = name
    f =  open("data.txt", "w")
    f.write(str(employees))  #We need a string to write in files thats why we used str()
    f.close()
    return id

def get_employee(id = 0):
    with open("data.txt", "r") as f:
        data = eval(f.read()) 
    if id == 0:    
        return data
    elif id in data:
        return data[id]
    else:
        return 0

def delete_employee(id):
    employees = get_employee()
    if id in employees:
        del employees[id]
        f =  open("data.txt", "w")
        f.write(str(employees))  #We need a string to write in files thats why we used str()
        f.close()
    else:
        return 0

