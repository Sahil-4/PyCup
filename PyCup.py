#Code Start
#Single Line Comment
"""
Multi
Line 
Comment
"""
"""
In Line 13 x is a variable 
And Hello is a string
"""
x = "Hello"
#Escape sequence in python
#In pythom backslash \ is escape character
print("print\x28\x22Hello world!\x22\x29")

#in Line 20 \b is backspace escape character
print(">", x ,end='\bworld!')
#in Line 22 \xhh is hex character in which hh is hex value ie:- \xh48
print("\n""\x48\x65\x6c\x6c\x6f" + " world")
#in Line 24 25 26 27 and 28 we saw String Slicing
print(x[2])
print(x[2:3])
print(x[0::2])
print(x[::-1])
print(x[::-2])


#Sorting list Line 34 and 36
nums = [1,5,3,2,4,8,0,9,7]
print (nums ,end="\breal list\n")
nums.sort()
print(nums ,end="\bsorted list\n")
nums.reverse()
print (nums ,end="reverse sorted list\n")
#Because python start counting from Zero you should have to add one to know the exact lenght of integers
print(len(nums)+1 ,end= '  \x23Character lenght of list\n')
print(max(nums) ,end='   \x23Max Number in List\n')
print(min(nums) ,end='   \x23Min Number in List\n')
#Adding items in list
lst = ["A1" , "B2 ", "C3 ","D4 ", "E5", "F6 "]
print(lst)
print(len(lst))
#C
lst.append("G7")
print(lst)
print (len(lst))
#C
lst.insert(1 , "A1")
print(lst)
print(len(lst))
#C
lst.remove("A1")
print(lst)
print(len(lst))
#C
lst.pop()
print(lst)
print(len(lst))
#C
a = "1"
b = "2"
print(a + b)
#Numbers Swaping
a ,b = b, a
print(a + b)
#To find Type or Class
L1=["","",""] #List
print(type(L1))
T1=("","","") #Tuple
print(type(T1))
D1={''} #Set
print(type(D1))
Tup1=(a,b)
print(type(Tup1)) #tuple(immutable)
D1b={"":"","":"","":""} #Dict
print(type(D1b)) #dict
#Using Dictionary
Dic1={"A":"a" , "B":"b" ,"C":"c" ,"D":"d"}
print(type(Dic1)) #dict
print(Dic1["A"])
print(Dic1["B"])
print(Dic1)
Dic1["E"]="e"
print(Dic1)
Dic1["Mis"] ="take"
print(Dic1)
#Del func of Dict
del Dic1["Mis"]
print(Dic1)
#Copy func of Dict
Dic2 = Dic1.copy()
del Dic2["E"]
print(Dic2)
#Printing Value
print(Dic2["D"])
print(Dic2.get("D"))
Dic2.update({"E":"e"})
print(Dic2)
"""
Inpt = input()
print(Dic2[Inpt])
if input will E
then output will e
"""
#Sets
S1 = set() #set
print(type(S1))
print(S1)
S1.add(1)
S1.add(2)
S1.add(3)
print(S1)
#Set Functions
s2 = S1.union({2,3,4,5}) #copy set
print(s2)
s2 = S1.intersection({})
print(S1)
print(s2)
#if elif else statements
print("\x23for user input")
print("x1 = input()")
print("\x23if elif else statements")
print('if x = "1":')
print("    print(\x22Hello1\x22)")
print("elif x = \x222\x22:")
print("    print(\x22Hello 2\x22)")
print("elif x = \x223\x22:")
print("    print(\x22Hello 3\x22)")
print("else :")
print("    print(\x22Hello\x22)")

#Loops
#For Loop
#Printing list item with for loops
print("\x23List Item By Loops")
for item in lst:
    print(item)

lise = ["A",1,0,4,"N",3,2,"D"]
print(lise)
for item in lise:
  if str(item).isnumeric() and item<3:
    print(item)
#While Loop
print("\x23This will print while loop")
print("i = 0\nwhile \x28i<10\x29:\n\t\t\t\tprint\x28i\x29\n\t\ti=i+1")
print("\x23Above code will print 0 to 9 becouse of while statement")
i = 0
while (i<10):
    print(i)
    i= i+1
#Another While loop
print("\x23Another While loop")
print("while\x28True\x29\x3A\n\tinp = int\x28input\x28\x22\x22\x29\x29\n\tif inp==100\x3A\n\t\tbreak\nelse\x3A\n\t\tprint \x28\x22\x22\x29")
print("\x23Enter 100 to finish the process")
while(True):
  inp = int(input("\n"))
  if inp==100:
    break
else:
      print ("")
#One More While Loop
print("\x23One More While Loop")
print("a = 'loop'\nwhile\x28True\x29\x3A\n\tinp = str\x28input\x28\x22Please Enter The Secret Code\x3A\n\x22\x29\x29\n\tif inp == a\x3A\n\t\tbreak\nelse\x3A\n\tprint\x28\x22Try Again\x22\x29")
print("\x23Enter loop to finish the process")
a = 'loop'
while(True):
  inp = str(input("Please Enter The Secret Code:\n"))
  if inp == a:
    break
else:
  print("Try Again")
#Operators
print("Operators in Python")
aA1 = "Types of Operators:7 \nArithmetic operators\nAssignment operators\nComparison operators \nLogical operators \nIdentity operators\nMembership operators \nBitwise operators"
print(aA1)
#Operators
#Functions
print("Functions in Python")
#def function1(a,b)
aB1 = "Types of Functions: 2\n 1. Built-in Functions.\n 2. User Defined Functions."
print(aB1)
print("This is a User Defined function")
def funcname1(a,b):
  """#This function used to obtain square of two numbers"""
  square = (a+b)**2
  return square
#print(funcname1.__doc__)
print("def funcname1(a,b):\x23This is Function Name\n \t \x22\x22\x22#This function used to obtain square of two numbers\x22\x22\x22\x23This is Doc String\n \t square = (a+b)**2 \x23This is Function Work  \n \t\treturn square\x23This will return the above square Function\n \n\x23Use of Above Function\nprint(\x22(a+b)**2\x22)\nx = 2 \x23int(input(\x22Enter the value of a:\x22))\ny = 2 \x23int(input(\x22Enter the value of b:\x22))\nz1 = \x22Whole Square of\x22\nz3 = funcname1(x,y)\nprint(z1,x,'+',y,'is',z3)\nprint(funcname1.__doc__)")
print("(a+b)**2")
x = 2 #int(input("Enter the value of a:"))
y = 2 #int(input("Enter the value of b:"))
z1 = "Whole Square of"
z3 = funcname1(x,y)
print(z1,x,'+',y,'is',z3)
print(funcname1.__doc__)
#Try except Exception handling
num1 = 2
num2 = 2
print(num1,'+',num2,'=', num1 +num2)

num3 = 2
num4 = "e"
try:
        print(num3,'+',num4,'=', num3 + num4)
except Exception as p:
        print(p)

num3 = 2
num4 = 5
print(num3,'+',num4,'=',num3 +num4)

"""
#Working With Files
#Read File
filename = input("")
f = open(filename,"rt")
content = f.read()
print(content)
f.close()

#Read Line
filename = input("")
f = open(filename,"rt")
for line in f:
  print(line)
f.close()

#Write File
filename = input("")
f = open(filename,"w")
write = input("")
f.write(write)
f.close()

#Append File
filename = input("")
f = open(filename,"a")
write = input("")
f.write(write)
f.close()

#Read and Write Both
filename = input("")
f = open(filename, "r+")
write = input("")
f.write(write)

#Read Line
filename = input("")
f = open(filename, "rt")
print(f.readline()) #Read Only First Line

#Tell func
filename = input("")
f = open(filename, "rt")
print(f.tell()) #>>>0
print(f.readline())
print(f.tell()) #>>>1

#Seek func
filename = input("")
f = open(filename, "rt")
print(f.tell()) #>>>0
print(f.readline())
print(f.tell()) #>>>1
f.seek(0)
print(f.tell()) #>>>0

#With func
with open(filename ,"rt") as f:
  a = f.read()
print(a)
"""

#No Need to type close command
#Types of variables Globle & Local
print("Variable Types\n1. Global \n2. Local")
print("Global : Can Used by Whole Program\nLocal : Can Used by a Particular Function in Program")
#Recursion:itertiv & rcursiv
"""
def rec1(str):
  rec1(str)
  print(str)
rec1("hello")
#>>>RecursionError Maximum depth exceeded
"""
"""
#Iterative Aproach
def faco1(n):
  fac = 1
  for i in range(n):
    fac = fac*(i+1)
  return fac
x = int(input(""))
print(faco1(x))
"""
"""
#Recursive Aproach
def fakR(n):
  if n == 1:
    return 1
  else:
    return n * fakR(n-1)
num = int(input())
print(fakR(num))
"""
"""
#Lambda or Anonymous function
#Normal function
def add(x,y):
  return x+y
#Lambda function
a= lambda x,y:  x+y
print(a(2, 4))

print((lambda x,y:  x-y)(2,4)
)

"""
"""
#Args&Kwargs
a ="Some"
b ="thing"
c =3
#Normal Str
print("This is",a+b,c

#FString
print(f"This is {a}{b} {c}")

"""
#Enumerates
ls =["Even", "Odd", "Even", "Odd", "Even"]
for index, item in enumerate(ls):
  if index%2==0:
    print(item)
print()
ls2 =["Even", "Odd", "Even", "Odd", "Even"]
for index, item in enumerate(ls):
  if index%2!=0:
    print(item)
#import
"""
//root/funt3.py
def funt3(xpf):
  print(type(xpf))
  for item in xpf:
    print(item)
a =["Hello","Good Morning","Good Night"]
funt3(a)
"""
"""
import funt3

"""
"""
//root/funt3b.py
def funt3B(xpf):
  print(type(xpf))
  for item in xpf:
    print(item)
a =["Hello","Good Morning","Good Night"]
funt3(a)
if __name__=='__main__':
  print(main)
"""

"""
import funt3B

"""
#Join Func
lisst= ["0", "1", "2", "3"]
print(lisst ,end=" \n")
als=" and ".join(lisst)
print(als, end=" \n", )

print("")

#Map Func
#print(lisst)
sd =["1", "2", "3", "4", "5"]
print(sd[0:4], type(sd[0:4]))
print(sd[0], type(sd[0]))

mapd= list(map(int, sd))

alp= mapd[0:4]
print(alp[0], type(alp[0]))

#Reduce Func
from functools import reduce

list1 = [1,2,3,4,2]
num = reduce(lambda x,y:x*y, list1)
print(num)

num = 0
for i in list1:
  num = num + i
  print(num)

#Filter function
list2 = list(filter(lambda x:x%2==0 ,list1))
print(list2)
#Decorator
def dec1(func1):
    def nowexec():
        print("Executing now l1")
        func1()
        print("Executed l4")
    return nowexec

@dec1
def aarg():
    print("Argument l2")

dwff = dec1(aarg)
#dwff()
aarg()

#OOPS
#Object Oriented Programming System

# Classes - Template
# Object - Instance Of the Class

# DRY - Do not repeat Yourself

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

#A Function That print The All details of an Instance
def details(user):
  print("Name:",user.name)
  print("Color:",user.color)
  print("Value:",user.value)
  print("Age:",user.AgeGroup)
#Creating A Function That print The All details of an Instance
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
#Generator
def gen(n):
    for i in range(n):
#        print(i)
        yield i

g = gen(5)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())

for i in g:
    print(i)
#iter
#iterable iterating
h = "Hello"
ier = iter(h)


#print(iter(h).__next__())
print(ier.__next__())
print(ier.__next__())
for str in ier:
    print(str,end="")

print()

#for c in h:
#    print(c)

#LRU_Cache
import functools
import time

@functools.lru_cache(maxsize=3)
def taketime(p):
    n=3
    time.sleep(n)
    print(f"Takes {n} Seconds to Load.")
    print(p)

taketime("hello")
taketime("hello")
taketime("hello")
taketime("helo")
taketime("hello")


#Regular Expressions
import re
#print(re.__doc__)
#print(dir(re))

######################
######################
# re Metacharacter

import re
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
#print(x)


import re
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
#print(x)


import re
txt = "hello world"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
#print(x)


import re
txt = "hello world"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
#if x:
#  print("Yes, the string starts with 'hello'")
#else:
#  print("No match")


import re
txt = "hello world"
#Check if the string ends with 'world':
x = re.findall("world$", txt)
#if x:
#  print("Yes, the string ends with 'world'")
#else:
#  print("No match")


import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 0 or more "x" characters:
x = re.findall("aix*", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 1 or more "x" characters:
x = re.findall("aix+", txt)
#print(x)
#if x:
#    print("Yes, there is at least one match!")
#else:
#    print("No match")


import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall("al{2}", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "eggspam"
#a group created by surrounding the pattern with parentheses () can be given as an argument to metacharacters such as * and ?
x = re.search("(spam)+", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


######################
######################
#re Special Sequences

import re
txt = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", txt)
#print(x)
#if x:
#  print("Yes, there is a match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Return a match at every no-digit character:
x = re.findall("\D", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Return a match at every white-space character:
x = re.findall("\s", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Return a match at every NON white-space character:
x = re.findall("\S", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
#print(x)
#if x:
#  print("Yes, there is a match!")
#else:
#  print("No match")


######################
######################
#re Sets

import re
txt = "The rain in Spain"
#Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")

import re
txt = "The rain in Spain"
#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "The rain in Spain"
#Check if the string has any characters between a and n:
x = re.findall("[a-n]", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")

import re
txt = "The rain in Spain"
#Check if the string has not any characters between a and n:
x = re.findall("[^a-n]", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "8 times before 11:45 AM"
#Check if the string has any digits:
x = re.findall("[0-9]", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")

import re
txt = "The rain in Spain"
#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[0123]", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")

import re
txt = "8 times before 11:45 AM"
#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "8 times before 11:45 AM"
#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")


import re
txt = "8 times before 11:45 AM!"
#Check if the string has any + characters
#In sets, +, *, ., |, (), $,{} has no special meaning
x = re.findall("[!:]", txt)
#print(x)
#if x:
#  print("Yes, there is at least one match!")
#else:
#  print("No match")




#Code Ended