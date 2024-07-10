# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:04:11 2024

@author: Javeria Malik
"""
#Python Variables
#1
break=5
#shows error cuz break is a Python keyword

#2
birth_year=2000
current_year=2024
age=current_year-birth_year
print(age)

#3
first_name='Javeria'
last_name='Malik'
full_name='My full name is '+first_name+' '+last_name
print(full_name)

full_name2=f'My full name is {first_name} {last_name}. And my age is {age}.'
print(full_name2)

#4 - 1record, record-one, record^one and continue

#Numbers
num=17
format(num,'b')

#String
#1
street='Gulshan'
city='Karachi'
country='Pakistan'

address=street+' '+city+' '+country
print(address)

address2=f'{street} {city} {country}'
print(address2)

address3=f'{street}\n{city}\n{country}'
print(address3)

#2
statement='Earth revolves around the sun'
print(statement[6:14])
print(statement[-3:])

#3
f=5
v=2
print(f'I eat {v} veggies and {f} fruits daily')

#4
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.
s='maine 200 banana khaye'
s=s.replace('banana','samosa').replace('200', '10')
print(s)

#LISTS
#1
expenses=[2200,2350,2600,2130,2190]

print(expenses[1]-expenses[0])

print(expenses[0]+expenses[1]+expenses[2])
print(sum(expenses[:3]))

2000 in expenses

expenses.append(1980)
print(expenses)

expenses[3]=1930
print(expenses)

#2
heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append('black panther')
print(heros)

heros.remove('black panther')
print(heros)

heros.insert(3,'black panther')
print(heros)

heros[1:3]=['doctor strange']
print(heros)

dir(list)
heros.sort()
print(heros)

#IF
#1 i
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input('Enter the city:')

if city in india:
    print(f'{city} is in India')
elif city in pakistan:
    print(f'{city} is in Pakistan')
elif city in bangladesh:
    print(f'{city} is in Bangladesh')
else:
    print(f'idk where {city} is')
#1 ii
city1=input('Enter city1: ')
city2=input('Enter city2: ')

if (city1 in india) and (city2 in india):
    print('Both cities are in India')
elif (city1 in pakistan) and (city2 in pakistan):
    print('Both cities are in Pakistan')
elif (city1 in bangladesh) and (city2 in bangladesh):
    print('Both cities are in Bangladesh')
else:
    print('They dont belong to the same country')

#2
sugar=int(input("Please enter your fasting sugar level:"))
if sugar<80:
    print('Sugar is low')
elif sugar>100:
    print('Sugar is high')
else:
    print('Sugar is normal')
    

#FOR LOOP
#1
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

count=0
for i in result:
    if i == 'heads':
        count = count + 1
print("Heads count:", count)

#focus on += below. can also be written that way
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for item in result:
    if item == "heads":
        count += 1
print("Heads count: ",count)

#2
#Print square of all numbers between 1 to 10 except even numbers
for i in range(1,11):
    if i%2==1:
        print(i*i)
#can also be written like below. continue sends the execution to the start without moving next
for i in range(1,11):
    if i%2==0:
        continue
    print(i*i)

#3 (DIFFICULT)
expense_list = [2340, 2500, 2100, 3100, 2980]
#Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.
month_list = ['January','February','March','April','May']

exp=int(input('Enter your expense here:'))

month=-1

for i in range(len(expense_list)):
    if exp==expense_list[i]:
        month=i
        break
    
if month != -1:
    print(f'You spent {exp} in {month_list[month]}')
else:
    print(f'you didnt spend {exp} in any month')

#4
# Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

for i in range(1,6):
    print(f'You just ran {i} miles')
    tired=input("are you tired?")    
    if tired=="no":
        continue
    else:
        print(f'you didnt finish the race but you still ran {i} miles')
        break
else:
    print('congratulations you finished the race')   
 
#Another way to attempt this 
for i in range(5):
    print(f"You ran {i+1} miles") # i starts with zero hence adding 1
    tired = input("Are you tired? ")
    if tired == 'yes':
        break
if i == 4: # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")

#5
print('''
      *
      **
      ***
      ****
      *****
      ''')
# make the above program 
s=''
for i in range(5):
    s=s+'*'
    print(s)

#can also be done this way
for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)

#FUNCTIONS
#1
def calculate_area(base, height):
    return (1/2) * base * height
calculate_area(5, 4)

#2
def calculate_area(base, height,shape_type='triangle'):
    if shape_type=='triangle':
        return (1/2) * base * height
    elif shape_type=='rectangle':
        return base * height
    else: 
        print('error: please input triangle or rectangle')
calculate_area(5, 4, 'octagon')
#can be done this way
def calculate_area(dimension1,dimension2,shape="triangle"):
    if shape=="triangle":
        area=1/2*(dimension1*dimension2) # Triangle area is : 1/2(Base*Height)
    elif shape=="rectangle":
        area=dimension1*dimension2 # Rectangle area is: Length*Width
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area='None' # If user didn't supply "triangle" or "rectangle" as shape then return None
    return area
calculate_area(5, 4, 'rectangle')

#3
#Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,

def print_pattern(num):
    s=''
    for i in range(num):
        s+='*'
        print(s)
print_pattern(4)     

#DICTIONARY AND TUPLES
#1
country_pop={"China":143,"India":136,"USA":32,"Pakistan":21}
'''
Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21
add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
'''
#my solution
input_mode=input('Enter the mode to perform:')
if input_mode=='print':
    for k,v in country_pop.items():
      print(f'{k}==>{v}')
elif input_mode=='add':
    country=input('Enter country name:')
    if country in country_pop:
        print('It exists')
    else:
        population=int(input('Enter country population:'))
        country_pop[country]=population
        print(country_pop)
elif input_mode=='remove':
    country_remove=input('Enter country to remove:')
    if country_remove in country_pop:
        del country_pop[country_remove]
        for k,v in country_pop.items():
          print(f'{k}==>{v}')
    else:
        print(f'{country_remove} doesnt exist')
else:
    query=input('Check the population of:')
    if query in country_pop:
        print(f'Population of {query} is:', country_pop[query])
    else:
        print(f'{query} doesnt exist')

#the other solution (not mine but great solution using functions)
population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country=input("Enter country name to add:")
    country=country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p=input(f"Enter population for {country}")
    p=float(p)
    population[country]=p # Adds new key value pair to dictionary
    print_all()

def remove():
    country = input("Enter country name to remove:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country]
    print_all()

def query():
    country = input("Enter country name to query:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore")

def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")

def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()

#2
stock_prices= {
    "info":[600,630,620],
    "ril":[1430,1490,1567],
    "mtl":[234,180,160]}

#calculating avg individually
def calc_avg(stock_name):
    return sum(stock_prices[stock_name])/3
calc_avg("info")

#doing exercise 2a
def print_all_stocks():
    for stock,prices in stock_prices.items():
        average=(sum(prices)/len(prices))
        print(f'{stock} ==> {prices} ==> avg:{average}')

def add():
    stock_name=input("Enter the stock name to add:")
    stock_name=stock_name.lower()
    if stock_name not in stock_prices:
        price_add=float(input("Enter stock_price:"))
        stock_prices[stock_name]=[price_add]
    else:
        price_add=float(input("Enter price for existing stock:"))
        stock_prices[stock_name].append(price_add)
    print_all_stocks()

def main():
    op=input("Enter operation: (print, add)")
    op=op.lower()
    if op=='print':
        print_all_stocks()
    elif op=='add':
        add()
    else:
        print('Please insert correctly')

if __name__ == '__main__':
    main()

#3
import math
math.pi
def circle_calc(r):
    area=math.pi*r*r
    circumference=2*math.pi*r
    diameter=2*r
    print(f'area:{area}\ncircumference:{circumference}\ndiameter:{diameter}')
circle_calc(3.5)

#another complicated way. lets ignore
def circle_calc(radius):
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius
    diameter=2*radius
    return area, circumference,diameter

if __name__=="__main__":
    r=input("Enter a radius:")
    r=float(r)
    area, c, d = circle_calc(r)
    print(f"area {area}, circumference {c}, diameter {d}")

#READ AND WRITE FILES
#1
with open("C:\\Users\\Javeria Malik\\Downloads\\data-science-roadmap-2024\\Python- Month 1\\poem.txt", "r") as f:
    f=f.read()

word_stats={}
words=f.split()
for word in words:
    if word in word_stats:
        word_stats[word] += 1
    else:
        word_stats[word] = 1

word_occurances = list(word_stats.values())
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_stats.items():
    if count==max_count:
        print(word)

#2
with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    next(f)  # This will skip first line in the file which is a header
    for line in f:
        tokens = line.split(",")
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price / eps, 2)
        pb = round(price / book, 2)
        out.write(f"{stock},{pe},{pb}\n")

#PLS REVIEW ERROR HANDLING IN NOTES

#CLASS AND OBJECTS
class Employee:
    def __init__(self,i,n):
        self.id=i
        self.name=n
    def display(self):
        print(f'ID:{self.id} Name:{self.name}')
        
emp=Employee(1,'coder')  
emp.display()        

del emp.id
# Deleting the object itself
try:
    print(emp.id)
except AttributeError:
    print("emp.id is not defined")

del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")
 

        
        