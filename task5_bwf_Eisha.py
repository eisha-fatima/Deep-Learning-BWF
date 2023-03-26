#Sets =>> Intro, Union, Intersection, Difference
set_eg = {"Book1","Book2","Book3"}
print(set_eg)

first_set={'cat','dog','lion'}
second_set= {'whale','shark','lion'}

union_set = first_set.union(second_set)
intersection_set = first_set.intersection(second_set)
diff_set = first_set.difference(second_set)
symmetric_diff = first_set.symmetric_difference(second_set)
print(union_set)
print(intersection_set)
print(diff_set)
print(symmetric_diff)


#enumerate function
names = ('Jon', 'Jones', 'Khan')
enumerated_set = enumerate(name)
print(list(enumerated_set))



# Conditionals
if('Eisha'=='Eisha'):
    print('two Strings are equal')
if('Lion'=='Eisha'):
    print('Same Strings')
else:
    print('Strings not equal.')

#Condtionals using lower method

if('Eisha'.lower()=='EISHA'.lower()):
    print('Equality Proved Using Lower function')

first_num = 10
second_num = 5
if(first_num==second_num):
    print('Proved')
if(first_num>second_num):
    print('Condtion Satisfied')
if(first_num<second_num):
    print('Condtion Satisfied')
if(first_num>=second_num):
    print('Condtion Satisfied')
if(first_num<=second_num):
    print('Condtion Satisfied')

#conditionals using 'in' & 'not in' 
list = ['house','lion','tiger']
if 'house' in list:
    print('String Present in the list')
if 'home' not in list:
    print('String no in list.')
    
    
#Excercise 5 => Q-> 5-4
alien_color = 'green'
if(alien_color=='green'):
    print('Player has won 5 Points.')
else:
    print('Player has won 10 points')

alien_color = 'red'
if(alien_color=='green'):
    print('Player has won 5 Points.')
else:
    print('Player has won 10 Points.')

    
#User Inputs
#Exercise 7
#=> Q=> 7-1
rentalcar = input('What kind of rental car do you like? ')
print('Customer likes '+rentalcar+' rental car.')

#-- Q -> 7-4
stay_in_loop = True
while stay_in_loop:
    topping = input('Enter the topping you need: ')
    if(topping == 'quit'):
        stay_in_loop = False
    else:
        print(topping + " topping added to the customers pizza.")
        
        
#--- Q -> 7-6
stay_in_loop = True
while stay_in_loop:
    topping = input('Enter the topping you need: ')
    if(topping == 'quit'):
        stay_in_loop = False
    else:
        print(topping + " topping added to the customers pizza.")
        
#Using Condition
stop = 0
while(stop!=4):
    print('Not Stopped Yet.')
    stop += 1

#Using Break
while stay_in_loop:
    topping = input('Enter the topping you need: ')
    if(topping == 'quit'):
        break
    else:
        print(topping + " topping added to the customers pizza.")

# Q => 7-7
#Infinite loop
while(True):
    print(input('Input: '))
