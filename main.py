#the file extension for python file is .py

#To run Your .py file simply run below command 
#$ python <filename.py> 
# $ python main.py 


#Comments in Python(3x)
#This is a Single Line Comment

"""
This is a
    Multi
        Line 
            Comment

"""

print("Hello Python!") #this is how we can print text on terminal 


#Simple Maths with Python 

#print(2 + 2)
#print(32 / 2)
#print(3 * 5)
#print(3 ** 3)
#print(5 % 2)
#print(5 // 2)

#print(2+2-1/2) #Output : 3.5
#print(((2+2)-1)/2) #Output : 1.5
#print(2+(2-1)/2) #Output : 2.5

# *to run any line simply uncomment the line (remove # from starting of the line)

#printing text on Screen 

print("This will be printed") #this will not be printed 

print("This \nis a way \nfor printing text on interpreter ") 
#here \n used to add a new line charactor in a string 

print("""
This 
is another way 
to print text on screen
""")


#Escape Charactors 
#    \'    Single Quote
#     \\    Backslash
#     \n    New Line
#     \r	Carriage Return
#     \t    Tab
#     \b    Backspace
#     \f    Form Feed
#     \ooo    Octal value
#    \xhh	Hex value

#we can also use excape charactors in variables or in strings


#variables in python

num = 0 #here num is variable name and 0 is the value of num 
#print(num) #printing vars value 

txt = "Hello" # we can make string variable with single or double Quote
#print(txt)


#Commonly used naming conventions for variable names 
"""
	1. camelCase 
	2. snake_case 
	3. PascalCase 

"""
"""
Some Valid Variable names

var1
name
myName
MyName 
my_name_is
My_Name
MYNAMe
etc.

You Cant Start a variable name by Number 

"""
#python is a case sensitive programming language so myVar and myvar is two different things 

name = "Alpha"
print("My Name is "+ name) #this is how we can print variable name along with a string 
#here + operator is used to concate variable with string 
#You cannot Concate numbers with string through this method 

#lets see how to concate number with string 
age = 20
print("My Age is", age)

# we will learn more about other string methods below 

#Assign Value to Multiple Variables at a time 

x, y, z = 1, 2, 3 #this is how we can declare many vars in a single 
#print(x)
#print(y)
#print(z)

#while assigning multiple variables at a time remember the order of index 


#Taking User input
#user = input() #this is the syntax for taking input from keyboard 

#x = input("Enter some Text Here: ") #we can also show text while taking the input so user will get some idea about what type of data he/she have to input
#here we are assinging input value to variable x 

#print("You Enteted "+ x) 

"""
Quiz :
    take input from user and print it
1. Method 
user = input()
print(user)

2. Method
print(input()) #if we have only to take input and print it without doing any operation on it

"""

#Operators in python 
"""
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
"""
#To Learn more about python Operators see pyOperatos.py










#Python Data Types 
"""
python Built-in Data Types: 

Text Type:	str

Numeric Types:	int, float, complex

Sequence Types:	list, tuple, range

Mapping Type:	dict

Set Types:	set, frozenset

Boolean Type:	bool

Binary Types:	bytes, bytearray, memoryview
"""

#Text Type : String
# to create a string simply use single or double quotes 
a = "This is a String"
a2 = "another String" # another string NOT a integer 
#print(a)


#String Methods and Operations 
#print(a + a2) #string concatenation 
#print(a +" "+ a2) #another way of string concatenation 
#print(a, a2) #one more way of string concatenation 

#print("2"+"2") #String Concatenation 

#print("Repeat 3 Times "*3) # repeatedly printing a string 3 times 
#print("2"*3) #repeating string 


#More String Methods 






