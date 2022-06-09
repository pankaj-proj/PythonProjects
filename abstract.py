import logging as log
from abc  import ABC,abstractmethod
# purpose:- To demostrate abstraction (base class)
# functionality:- There are different implementation of salary method in child classes (employee and manager)
class calculate_salary(ABC):
    @abstractmethod
    def salary(self): #abstract method to define salary, child class method can give own implimentation
        pass

class employee_salary(calculate_salary):
    base_salary=0
    salary_hike=5 # 5% salary hike for employee
    # parameterized constructor
    def __init__(self, sal):
        try:
            self.base_salary = sal
        except Exception as e:
            log.error('Exception while calculating employee salary ' + e)
    def salary(self):  # Hike employee salary to 5 percent
        try:
         return self.base_salary+(self.base_salary*self.salary_hike/100) #calculating employee salary
        except Exception as e:
            log.error('Exception while employee salary hike calculation ' + e)

class manager_salary(calculate_salary):
    base_salary=0
    salary_hike= 10 # 10% salary hike for employee

    # parameterized constructor
    def __init__(self, sal):
        self.base_salary = sal
    def salary(self):  # Hike manager salary to 10 percent
        try:
            return self.base_salary+(self.base_salary*self.salary_hike/100) # calculating manager salary
        except Exception as e:
            log.error('Exception while manager salary hike calculation ' + e)

