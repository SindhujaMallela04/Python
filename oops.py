class Employee:
    def __init__(self, name, salary):
        self.__name = name        
        self.__salary = salary

    def get_name(self):
        return self.__name
    
    def set_salary(self, salary):
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def get_salary_after_allowances(self, allowances):        
        return self.__salary + sum(allowances)
    
    def get_salary_after_deductions(self, deductions):
        for i in deductions:
            if i < 0 or i > 100:
                print("Invalid Deduction Percentage")
                return
            else:
                self.__salary = self.__salary - (self.__salary * i / 100)
        return self.__salary       
    

emp_name = input("enter the Employee Name: ")
emp_salary = int(input("Enter the employee Salary: "))
emp = Employee(emp_name, emp_salary)

allowances_list = list(map(int, input("Enter the Allowances: ").split()))
deductions_list = list(map(int, input("Enter the Deductions in percentage: ").split()))

salary_after_allowance = emp.get_salary_after_allowances(allowances_list)
salary_after_deductions = emp.get_salary_after_deductions(deductions_list)

print(f"Gross salary after issue of Allowance: {salary_after_allowance}")
print(f"Salary after Tax Deductions: {salary_after_deductions}")

print()