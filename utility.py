import Employee
import os

def check_employee():
    id = int(input("Enter id please: "))
    emp = Employee.get_employee(id)
    if emp == 0:
        print("Employee not found")
    else:
        print(f"Employee found with name: {emp}")

def adding_employee():
    name = input("Please enter your name: ")
    id = Employee.add_employee(name)
    print(f"New employee added with id: {id}")

def deleting_employee():
    id = int(input("Enter id to delete:"))
    if Employee.delete_employee(id) != 0:
        print(f"User deleted with id {id}")
    else:
        print(f"No id matched to delete")
        
def get_all_employee():
    employees = Employee.get_employee()
    print("All Employee List - ")
    for id, name in employees.items():
        print(f"{id}: {name}")

def print_menu():
    print("--- Options ---")
    print("Press 1 to check employee")
    print("Press 2 to add employee")
    print("Press 3 to delete employee")
    print("Press 4 to display all employee")
    print("Press 5 to clear the screen")
    print("Press 6 to exit")

def clear_screen():
    os.system('cls')
    print_logo()

def print_logo():
    print(r"""
    _______
   /      /,
  /      //
 /______//
(______(/
    
    """)