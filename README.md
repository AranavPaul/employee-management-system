# Employee Management System (File Handling) - Python

A simple **CLI-based** Employee Management System built in Python using file handling.  
It stores employee records in a `data.txt` file and provides options to add, search, delete, and display employees.

---

## Features
- Check employee by ID
- Add a new employee (auto-generates a random ID)
- Delete employee by ID
- Display all employees
- Clear screen option (Windows)

---

## Project Structure
```text
employee-management-system/
│── main.py        # Main program (run this file)
│── utility.py     # Menu + input/output functions
│── employee.py    # File handling + employee operations (read/write data.txt)
│── data.txt       # Stores employee records
│── README.md

How it works 
main.py runs an infinite loop, shows a menu, and calls functions from utility.py.

utility.py takes user input and calls methods from employee.py.

employee.py reads/writes data.txt and stores employee info as a dictionary like:
{employee_id: 'employee_name'}


Requirements
Python 3.x installed on your system


Setup & Run
Option A: Run directly (recommended for beginners)
Download (or clone) this repository.

Make sure these files are in the same folder:
main.py, utility.py, employee.py, data.txt

Open Terminal / CMD in that folder.

Run: python Code.py

Option B: If python command doesn’t work
Try: python3 main.py


Usage
When you run the program, you will see menu options like:

Press 1 to check employee

Press 2 to add employee

Press 3 to delete employee

Press 4 to display all employee

Press 5 to clear the screen

Press 6 to exit

Example:

Choose 2 → enter a name → it will generate an ID and save it in data.txt.

Choose 1 → enter an ID → it shows employee name if found.

Choose 4 → lists all employees stored in the file.


Data Storage Format (data.txt)
The employee data is saved inside data.txt in dictionary format, for example:
{3: 'Komal', 920121562: 'ritik', 557923563: 'neha'}


Notes / Limitations
Current implementation reads file data using eval().
For learning projects it may work, but for real projects it is safer to use json (JSON file format) instead.

clear screen uses cls, which works on Windows. On Linux/macOS you may need to change it to clear.


Author
Aranav Paul

