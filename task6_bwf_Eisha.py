#Dictionaries
# Adding,Removing from Dictionary and Modifying Dictionary 
person = {
    'name':'eisha'
}
print(person)
person['age'] = 21
print(person)
del person['name']
print(person)
person['age'] = 11
print(person)

#Exercise 6
#-- Q -> 6-1
person = {
    'first_name':'Sana',
    'last_name':'Khan',
    'Degree':'Software'
}
print("Person's Detail: ")
print(person['first_name'])
print(person['last_name'])
print(person['degree']+'\n')

# -- Q -> 6-2
favorite_numbers = {
    'Eisha':7,
    'Fatima':21,
    'Alina':24,
}
print("Eisha's favorite number is: "+str(favorite_numbers['Eisha']))
print("Fatima's favorite number is: "+str(favorite_numbers['Fatima']))
print("Alina's favorite number is: "+str(favorite_numbers['Alina']))

print()
print()


# --- Q -> 6-5
rivers = {
    'Nile':'Egypt',
    'Amazon':'Peru',
    'Sutlej':'Pakistan',
    'Ganga':'India'
}
for river,country in rivers.items():
    print(river+" runs through "+country)
for river,country in rivers.items():
    print(river)
for river,country in rivers.items():
    print(country)


# ---- Q -> 6-7
dictionary1 = {
    'name':'Eisha',
    'age':'21',
}
dictionary2 = {
    'name':'Sana',
    'age':'22',
}

dictionary3 = {
    'name':'xzy',
    'age':'23'
}


people = [dictionary1,dictionary2,dictionary3]

for person in people:
    print('Name: '+person['name'])
    print('Age: '+person['age'])
    
# -- Q -> 6-10
fav_numbers_list = {
    'Eisha':[20,321,345],
    'Sana':[7,911,283],
    'Alina':[123,2763,7373]
}

for name,favourite_numbers in fav_numbers_list.items():
    print(name)
    print('Favourite Numbers: ')
    for no in favourite_numbers:
        print(no)

# -- Q -> 6-11
city_dictionary = {
    'Texas':{
        'Country':'USA',
        'Population':'1100000',
        'Fact':'Cowboys'
    },
    'London':{
        'Country':'UK',
        'Population':'555005000',
        'Fact':'Oxford'
    },
    'Chicago':{
        'Country':'USA',
        'Population':'1233839',
        'Fact':'Home of US'
    }
}

for city,details in city_dictionary.items():
    print("\n City: "+ city)    
    print("Country: "+details['Country']+'\n'+'Population: '+details['Population']+
          '\n'+'Fact: '+details['Fact']+'\n')
