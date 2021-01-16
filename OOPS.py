#Class
class Employee: #Defining Class
    Head = "Alpha" #Class Variable
    Post = "Employee"
    def __init__(self, fnAme, lnAme, Age, sAlary): #Dunder init or instantiation class method
        self.fname = fnAme
        self.lname = lnAme
        self.age = Age
        self.salary = sAlary

#Property decorator
    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@eMail.com"

#Setter
    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

#Deleter
    @email.deleter
    def email(self):
#        self.email = None
        self.fname = None
        self.lname = None

class Programmer(Employee): #Single Inheriting Class
    #super().__init__()
    #self.head = "Alpha"
    Post = "Programmer"

class Head(Programmer): #Multi Inheriting
    Post = "Head"
    Head = 0
#ClassMethod and StaticMethod
    @classmethod #Creating class method to change Class Head
    def chng_Head(cls, newHead):
        cls.Head = newHead

    @staticmethod #Creating A Staticmethod it doesn't required class'
    def  prit(nAme):
        return f"Hello {nAme}"

#Creating A Function
def printer(self): #Function That print all details of given instance
    return f"Name: {self.fname} {self.lname}\nAge: {self.age}\nSalary: {self.salary}\nPost: {self.Post}\nHead: {self.Head}\n"

#Instances
Emp1 = Head("Alpha", "X", 19, "$200") #An instance of Class Head and its instance varias
Emp2 = Programmer("Bets", "Y", 16, "$150") #An instance of Class Programmer
Emp3 = Employee("Gamma", "J", 13, "$50") #An instance of Class Employee

#printing Result
print(printer(Emp1))
print(printer(Emp2))
Employee.Head = "Beta"
print(printer(Emp3))
print(printer(Emp1)) #becoause we created its ows instance variable Head = "0" thats why it's Head doesn't changed'
print(Head.prit("Alpha")) #Using Static Method

print(Emp3.fname,"'s Email:",Emp3.email)
Emp3.email = "Gama.Mail@eMail.com"
print(Emp3.fname,"'s New Email:",Emp3.email)
del Emp3.email
print(Emp3.email)

