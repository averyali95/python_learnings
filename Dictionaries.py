""" Dictionaries
    Dictionaries are a built-in Python data structure for mapping keys to values.    """

numbers = {'one': 1, 'two': 2, 'three': 3}
# In this case, the keys are 'one', 'two', and 'three' while the values are 1,2,3

# Values are accessed through square brackets[key](

print(numbers["one"])  # returns value of 1

# We can add another value, key pair using the syntax below.
numbers['eleven'] = 11
print(numbers)

# Dictionaries use comprehenstions similiar to list comprehensions
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

# The 'in' operator tells us if something is a key in the dictionary
print('Saturn' in planet_to_initial)  # return true
print('Betelgeuse' in planet_to_initial)  # return false

# A for loop over a dictionary will loop through key values and not the actual values
for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# We can access a collection of all the keys or all the values with dict.keys() and dict.values(), respectively.
print(' '.join(sorted(planet_to_initial.values())))

# The very useful dict.items() method lets us iterate over the keys and values of a dictionary simultaneously.
# (In Python jargon, an item refers to a key, value pair)

# in planet_to_initial.items() allows to iterate over whole dictionary, key and value
for planet, planet_initial in planet_to_initial.items():
    print("{} beings with the letter \"{}\"".format(planet.rjust(10), planet_initial))  # rjust does a right align of items

"""
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
"""


breakfast_food = ["bacon", "cereal", "eggs", "french toast", "sausage", "hash brown", "oatmeal"]
breakfast_menu = []
breakfast_item_num = 1
order_menu = {}
for item_name in breakfast_food:
    breakfast_menu.append(str(breakfast_item_num) + item_name[0].upper())
    breakfast_item_num += 1

#Zip function lets you iterate through two lists at the same time
for food, item_num in zip(breakfast_food, breakfast_menu):
    order_menu[item_num] = food

print(order_menu)

