"""
String syntax
You've already seen plenty of strings in examples during the previous lessons, but just to recap, strings in Python can
be defined using either single or double quotations. They are functionally equivalent.
"""
x = 'Pluto is a planet'
y = "Pluto is a planet"
print(x == y)

"""

The table below summarizes some important uses of the backslash character.

What you type...	What you get	example	print(example)
\'	'	'What\'s up?'	What's up?
\"	"	"That's \"cool\""	That's "cool"
\\	\	"Look, a mountain: /\\"	Look, a mountain: /\
\n	"1\n2 3"	1
                23
"""

hello = "hello\nworld"
print(hello)

"""
In addition, Python's triple quote syntax for strings lets us include newlines literally (i.e. by just hitting 'Enter' on our keyboard, rather 
than using the special '\n' sequence). We've already seen this in the docstrings we use to document our functions, but we can use them anywhere
 we want to define a string.
"""
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print(triplequoted_hello == hello)

"""The print() function automatically adds a newline character unless we specify a value for the keyword argument end other than the 
default value of '\n':
"""
print("hello")
print("world")
print("hello", end='')
print("pluto", end='')

"""
Strings are sequences
Strings can be thought of as sequences of characters. Almost everything we've seen that we can do to a list, we can also do to a string.
"""
# Indexing
planet = 'Pluto'
planet[0]

# Slicing
planet[-3:]

# How long is this string?
len(planet)

# Yes, we can even loop over them
[char+'! ' for char in planet]

#We cannot modify strings though, they are immutable

#String Methods
# ALL CAPS
claim = "Pluto is a planet!"
claim.upper()

# all lowercase
claim.lower()

# Searching for the first index of a substring
claim.index('plan')

#
claim.startswith(planet)

# false because of missing exclamation mark
claim.endswith('planet')

"""
Going between strings and lists: .split() and .join()
str.split() turns a string into a list of smaller strings, breaking on whitespace by default. This is super useful for 
taking you from one big string to a list of words.
"""

words = claim.split()
print(words)

datestr = "1956-02-21"
year, month, day = datestr.split('-')
print(year, month, day)

#join - combines list of strings into one long string using a seperator.
print('/'.join([month, day, year]))

# Yes, we can put unicode characters right in our string literals :)
print(' 👏 '.join([word.upper() for word in words]))

"""
Building strings with .format()¶
Python lets us concatenate strings with the + operator.
"""

print(planet + ", We miss you")

# if we want to throw non-string type data, we must use the str() function to convert to a string
position = 9
print(planet + ", You will always be me the " + str(position) + "th planet to me")

#or we can use the format function using {}
print("{} you will always be the {}th planet to me".format(planet, position))

"""So much cleaner! We call .format() on a "format string", where the Python values we want to insert are represented 
    with {} placeholders.

Notice how we didn't even have to call str() to convert position from an int. format() takes care of that for us."""

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

#             2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

