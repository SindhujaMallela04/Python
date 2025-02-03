from abc import ABC, abstractmethod
from typing import List
import csv

# Step 1: Define Employee interface using Abstract Base Class (ABC)
class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass
    
    @abstractmethod
    def get_salary(self) -> float:
        pass


# Step 2: Create concrete classes for different types of employees

class Manager(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is managing the team."

    def get_salary(self) -> float:
        return self.salary


class Developer(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is writing code."

    def get_salary(self) -> float:
        return self.salary


class Intern(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is learning and assisting."

    def get_salary(self) -> float:
        return self.salary


# Step 3: Define Department class that manages Employees

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired.")

    def promote(self, employee: Employee) -> None:
        if isinstance(employee, Intern):
            employee.__class__ = Developer
            employee.salary = 60000
            print(f"{employee.name} has been promoted to Developer, his salary is {employee.salary}.")
        elif isinstance(employee, Developer):
            employee.__class__ = Manager
            employee.salary = 80000
            print(f"{employee.name} has been promoted to a Manager, his salary is {employee.salary}.")
        elif isinstance(employee, Manager):
            employee.salary = 100000
            print(f"{employee.name} has been promoted to CEO, his salary is {employee.salary}.")
        elif isinstance(employee, Security):
            employee.salary = 10000
            print(f"{employee.name} has been promoted to Sr. Security Officer, his salary is {employee.salary}.")
           
    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired.")

    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employees)

    def show_employee_details(self) -> None:
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(f"- {employee.name}, Salary: {employee.get_salary()}, Role: {employee.work()}")

class Security(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is Securing the assets."

    def get_salary(self) -> float:
        return self.salary
    

def save_employee_details_to_csv(department: Department, filename: str) -> None:
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Role", "Salary"])
        for employee in department.employees:
            writer.writerow([employee.name, employee.work(), employee.get_salary()])

def read_employee_details_from_csv(filename: str) -> None:
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)



# Create employees
manager = Manager("Alice", 80000)
developer = Developer("Bob", 60000)
intern = Intern("Charlie", 20000)
securitystaff=Security("Ram",5000)

# Create a department and hire employees
it_department = Department("IT")

it_department.hire(manager)
it_department.hire(developer)
it_department.hire(intern)
it_department.hire(securitystaff)
# Show employee details
it_department.show_employee_details()

it_department.promote(intern)
it_department.promote(developer)
it_department.promote(securitystaff)

# Save employee details to a CSV file
save_employee_details_to_csv(it_department, 'employee_details.csv')
read_employee_details_from_csv('employee_details.csv')

# Total salary in the department
total_salary = it_department.get_total_salary()
print(f"Total salary expense for {it_department.name} department: ${total_salary}")






