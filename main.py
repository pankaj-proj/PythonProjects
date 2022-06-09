# This is a sample Python script.

from abstract import employee_salary,manager_salary
from multipleInheritance import employee,employeeRating,employeePerformance
from filemanagment import filemanagment
from filemanagment import filemanagment
from logger import configurelogger



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # configure logger
    configurelogger();

    # file replacement task
    filemanagmentobj = filemanagment();
    filemanagmentobj.replace_text('C:\Input\example.txt','placement','screening')

    #abstract class example
    employee_object = employee_salary(5000)
    print(employee_object.salary())

    manager_object = manager_salary(10000)
    print(manager_object.salary())

    # multiple inheritance
    employeePerformance = employeePerformance();
    employeePerformance.getEmployeePerformance();
    employeePerformance.printEmployeePerformanceDetail();


