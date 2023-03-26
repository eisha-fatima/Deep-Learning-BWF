#Functions
#Exercise 8
# ---- Q ->>> 8-1
def display_message():
    print('Learning of Python methods or functions in this chapter.\n')
display_message()

# ---- Q ->>> 8-2
def favourite_book(title):
    print('Myy favourite book is '+title+'.\n')
favourite_book('Game of Thrones')

# ---- Q ->>> 8-4
def make_shirt(size="Large",text="I Love Python."):
    print('Size of the Shirt: '+size+'\nMessage on the Shirt: '+text+'\n')
make_shirt()
make_shirt('medium')
make_shirt("small","I want to win the World.")


#Return Values
# ---- Q ->>> 8-6
def city_country(name,country):
    info = '"'+name+', '+country+'"'+'\n'
    return info
print(city_country('Chicago','USA'))
print(city_country('London','UK'))
print(city_country('Chennai','India'))


# ---- Q ->>> 8-7
def make_album(artist,title,Tracks_count=0):
    if(Tracks_count==0):
        Album_details={
            'Artist Name': artist,
            'Album_Title': title
        }
    else:
        Album_details = {
            'Name of the Artist': artist,
            'Title of Album': title,
            'No of Tracks on the Album': Tracks_count
        }
    return Album_details
print(make_album('Billie','Lovely'))
print(make_album('John Legend','Legend'))
print(make_album('Coldplay','Stars',12))

#Arbitrary Arguments
# ----- Q ->>> 8-12
def sandwiches(*flavours):
    print('Flavours: '+flavours)
    
sandwiches('Mayo')
sandwiches('Cheeese','Ketchup')
sandwiches('Chicken','Sauce','Salad')
