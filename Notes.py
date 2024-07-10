# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:47:04 2024

@author: Javeria Malik
"""
#run for exp
exp = [2500, 2300, 1000, 5000]
exp.append(3000)
exp.insert(3, 500)
print(exp)

total = 0
for i in exp:
    total = total + i
print(total)

for i in range(1,11):
    print(i)

#output with total expense with each month
total=0
for i in range(len(exp)):
    print("Month:", (i+1), "Expense:", exp[i])
    total=total+exp[i]
    print("My total expense is:", total)

#output with total expense only once
total=0
for i in range(len(exp)):
    print("Month:", (i+1), "Expense:", exp[i])
    total=total+exp[i]
print("My total expense is:", total)

#Searching for key and stopping at key location
key_location=["chair"]
locations=["garage","living room","chair","closet"]

for i in locations:
    if i in key_location:
        print("key is found in:", i)
        break        
    else:
        print("key is not found in:", i)

#Calculating squares of numbers that are not even
#The continue code below skips the remaining code after continue and moves on the for loop
for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)
 
#doing the same thing 2 different ways    
i=1
while i<=5:
    print(i)
    i=i+1

for i in range(1,6):
    print(i)

#FUNCTIONS
#expense function

jav_exp_list=[200,300,500,1500]
hira_exp_list=[350,550,600,1800]

def calculate_total(exp):
    total=0
    for i in range(len(exp)):
        print("Month:", (i+1), "Expense:", exp[i])
        total=total+exp[i]
    print("Total expense is:", total)
    return total
    
jav_total=calculate_total(jav_exp_list)
hira_total=calculate_total(hira_exp_list)

print("Jav's total expense is:", jav_total)
print("Hira's total expense is:", hira_total)


#sum function
def sum(a,b):
    total=a+b
    return total

n=sum(6,5)
print("Total:",n)

#subtract function with default b value. if I give b value then default value overwrites
#return is to store value to the variable
def subtract(a,b=1):
    print("a:", a)
    print("b:", b)
    result=a-b
    print("The result of subtraction is:", result)
    return result

subtract(11)
x=subtract(11)
print(n)

#check this
print("""This function is subtracting b from a.
      If b value is not given than default value returns.""")

#DICTIONARIES
d={"tom":732238794, "rob": 2984598375, "joe": 649068}
d
d["sam"]=9580385
d["joe"]
del d["sam"]
d
for key in d:
    print("key:", key, "value:", d[key])
#can also be written as
for k,v in d.items():
    print("key:", k, "value:", v)
#check if name in d    
"tom" in d
#remove everything from dict
d.clear()
d


#Tuples
point=(5,9) #x coordinate is 5 and y coordinate is 9
point[0]
#in tuples values have different meanings ie one is x coord and second is y coord
#in list all values have the same meaning ie all values are expenses or name etc

#modules in python
import math
math.sqrt(9)
math.pow(7,9)
math.pi

import calendar
cal=calendar.month(2024,2)
print(cal)
dir(calendar)
calendar.isleap(2024)

#importing the calc triangle function from the file in the same directory as my file
#set directory please
import areas
areas.calculate_triangle_area(3, 5)

#importing from the directory below
import sys
sys.path.append("C:\\Users\\Javeria Malik\\Downloads\\data-science-roadmap-2024\\Python- Month 1")
import areas as a
area= a.calculate_square_area(5)
print(area)

##JSON
book={}
book['tom'] = {'name': 'tom',
    'address': 'gulshan e iqbal',
    'phone': '0331823497'
    }
book['jav'] = {'name': 'jav',
    'address': 'gulshan e iqbal',
    'phone': '0333420097'
    }
import json
s=json.dumps(book)
#write the json format s string into a book.txt
with open("C:\\Users\\Javeria Malik\\Downloads\\data-science-roadmap-2024\\Python- Month 1\\book.txt", "w") as f:
    f.write(s)

#reading the book.txt file
f=open("C:\\Users\\Javeria Malik\\Downloads\\data-science-roadmap-2024\\Python- Month 1\\book.txt", "r")
s=f.read()
s
import json
book=json.loads(s)
#checking tupes
type(s)
type(book)
book['jav']['phone']
for person in book:
    print(book[person])

#this below is the key value format from where we use the whole person values and print phone
for person, values in book.items():
    print(values['phone'])
#printing only person and phone values
for person, values in book.items():
    print(person, values['phone'])

#name main
__name__
#the __name__ value is main here cuz it is main file. 
#if we import the function in another file then the value would be file name

#EXCEPTIONS
x=input('x value:')
y=input('y value:')
try:
    z=int(x)/int(y)
except Exception as e:
    print('exception occured:', e)
    z=None
print("Division is:", z)

#the response will be 
#x value:10
#y value:0
#exception occured: division by zero
#Division is: None

#setting a specific exception; ie division by zero
#Exceptions
x=input('x value:')
y=input('y value:')
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print('Division by Zero exception:', e)
    z=None
print("Division is:", z)

#we cant divide int by str
#To figure out what exception this causes we will run this
x=input('x value:')
y=input('y value:')
try:
    z=x/int(y)
except ZeroDivisionError as e:
    print('Division by Zero exception:', e)
    z=None
except Exception as e:
    print('exception type:', type(e).__name__)
print("Division is:", z)

#below will be the response
"""x value:20
y value:3
exception type: TypeError
Division is: None"""

#we fix it like this for future anticipated errors and we can also remove (,e) if detail not required
x=input('x value:')
y=input('y value:')
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print('Division by Zero exception:', e)
    z=None
except TypeError as e:
    print('type error exception', e)
print("Division is:", z)

#CLASS AND OBJECTS
#self is the class itself
#name and .occupation are properties of class Human 
#n and o are arguments of the function
class Human:
    def __init__(self, n, o):
        self.name=n
        self.occupation=o
    def do_work(self):
        if self.occupation == "tennis player":
            print (self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots a film")
    def speaks(self):
        print(self.name, "says how are you?")

tom=Human("tom cruise", "actor")
tom.do_work()
tom.speaks()



