primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

my_favourite_things = [32, 'raindrops on roses', help] #you can mix data types in a list

#indexing allows you to access different parts of a list using numberic values.
print(hands[0])
print(planets[-1]) #returns first element from the end of the list

#slicing allows you to select element of the list using start and ending notation
print(primes[0:3]) #this will print starting at the zero index to the seoncd index value
print(primes[:3]) #this is the same as above as it is assumed the first index

print(planets[3:]) # prints from the third index on to the end of the list

# The last 3 planets
print(planets[-3:])

# All the planets except the first and last
print(planets[1:-1])

#Changing lists, lists are mutable, meaning they can be modified
#say we want to rename mars.
planets[3] = "Mars2"
print(planets[3])

#we can also change multiple values at a time
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

# List functions
#len() gives you the length
print(len(planets))

# The planets sorted in alphabetical order
print(sorted(planets))

primes = [2, 3, 5, 7]
print(sum(primes))

#min and max
print(min(planets)) #Even works on non-numeric values   
print(max(primes))

#Tuples are almost exactly the same as lists. They differ in just two ways.
# 1: The syntax for creating them uses parentheses instead of square brackets
# 2: They are immutable and cannot be changed once created
t = (1, 2, 3)
print(t)

# Tupples are often used when you have to return multiple values during a function

num = .125
# as_integer_ratio changes decimal into numerator and denominator
print(num.as_integer_ratio())

# two assignment within one assignment clause
numerator, denominator = num.as_integer_ratio()
print(numerator/ denominator)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    """team = teams[-1]
    return team[1]"""
    return teams[-1][1] # -- gives you the same result


def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.

    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0], racers[-1] = racers[-1], racers[0]


def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late. A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, they must not be the very
    last guest (that's taking it too far). In the above example, Mona and Gilbert are the only guests who were fashionably late.
    """
    """order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1
    """
    order = arrivals.index(name)
    arrivals_size = len(arrivals)
    half_party = len(arrivals) / 2

    if order >= half_party and order != arrivals_size - 1:
        return True
    else:
        return False

party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford' ]
print(fashionably_late(party_attendees,'Ford' ))

"""
    Iterration through a list while comparing indicies. We must use the range function
"""

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for index in range(len(meals)-1): #the range function he will have us perform the loop to the last value of the list
        if meals[index] == meals[index+1]:  #compare the value at the current index, too the following index
            return True
    return False

