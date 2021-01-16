#python 3.7.1
#Created by 
#Feel free to use this code
#Code Start
"""
THIS CODE DOESN'T 
WORK ON SOLOLEARN 
USE THIS CODE
 ON
OTHER Python IDEs 
 
"""
#if you have any suggestion about this code then please comment it down.
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

#No Need to type close command

"""
#Extra Instructions
FILE MODES:

"r"
Read from file - YES
Write to file - NO
Create file if not exists - NO
Truncate file to zero length - NO
Cursor position - BEGINNING

"r+"
Read from file - YES
Write to file - YES
Create file if not exists - NO
Truncate file to zero length - NO
Cursor position - BEGINNING

"w"
Read from file - NO
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - YES
Cursor position - BEGINNING

"w+"
Read from file - YES
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - YES
Cursor position - BEGINNING

"a"
Read from file - NO
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - NO
Cursor position - END

"a+"
Read from file - YES
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - NO
Cursor position - END

"""
#Code Ended
