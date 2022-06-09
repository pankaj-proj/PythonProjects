import logging as log
# purpose:- To demostrate multiple inheritance
# functionality:- EmployeePerformance class will use employee and employee rating class to complete functionality
class employee:
    _employeename=""
    def getEmployeeDetail(self):
        try:
            self._employeename = input("Enter Employee Name")
        except Exception as e:
            log.error('Exception while getting employee detail ' + e)
    def printEmployeeDetail(self):
        try:
          print("Employee detail ", self._employeename)
        except Exception as e:
            log.error('Exception while printing employee detail ' + e)

class employeeRating:
    _rating = 0;
    def getEmployeeRating(self):
        try:
            self._rating = int(input("Enter Employee Rating: "))
        except Exception as e:
            log.error('Exception while getting employee rating ' + e)
    def printEmployeeRating(self):
        try:
            print("Empoyee rating is ",self._rating)
        except Exception as e:
            log.error('Exception while printing employee rating ' + e)


class employeePerformance(employee,employeeRating):
    def getEmployeePerformance(self):
        try:
            self.getEmployeeDetail()
            self.getEmployeeRating()
        except Exception as e:
            log.error('Exception while getting employee performance detail ' + e)

    def printEmployeePerformanceDetail(self):
        try:
            self.printEmployeeDetail()
            self.printEmployeeRating()
        except Exception as e:
            log.error('Exception while printing employee performance detail ' + e)