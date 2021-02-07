print("******COMPANY MANAGEMENT SYSTEM********")
print("--MANAGERS--")

class Manager:
    def __init__(self, mFirstName, mLastName, mAges):
        self.ManagerFirstName = mFirstName
        self.ManagerLastName = mLastName
        self.ManagerFullName = mFirstName + mLastName
        self.ManagerAges = mAges
    def printManagerName(self):
        print(self.ManagerFirstName + self.ManagerLastName)
    def printManagerAge(self):
        print(self.ManagerFullName + " is " + str(self.ManagerAges) + " years old.")
    def ManagerStatus(self):
        print(self.ManagerFullName + " is a manager and " + str(self.ManagerAges) + " years old.")

manager1 = Manager("Onyedikachi", " Uzoma", 40)
manager1.printManagerName()
manager1.printManagerAge()
manager1.ManagerStatus()

print("--EMPLOYEES--")


class Employees:
    def __init__(self, eFirstName, eLastName, eAges, eLanguages):
        self.EmployeesFirstName = eFirstName
        self.EmployeesLastName = eLastName
        self.EmployeesFullName = eFirstName + eLastName
        self.EmployeesAge = eAges
        self.EmployeesLanguages = eLanguages
    def printEmployeesName(self):
        print(self.EmployeesFirstName + self.EmployeesLastName)
    def printEmployeesAge(self):
        print(self.EmployeesFullName + " is " + str(self.EmployeesAge) + " years old.")
    def EmployeesStatus(self):
        print(self.EmployeesFullName + " is an employee and " + str(self.EmployeesAge) + " years old.")
    def printLanguages(self):
        print(self.EmployeesFullName + " can speak:" + self.EmployeesLanguages)
        
employees1 = Employees("Chidi", " Anosike", 27, " Spanish " + " English " + " Turkish ")
employees1.printEmployeesName()
employees1.printEmployeesAge()
employees1.EmployeesStatus()
employees1.printLanguages()

print("--EMPLOYEE LANGUAGES--")

employees1.printLanguages()
