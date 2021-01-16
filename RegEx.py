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

