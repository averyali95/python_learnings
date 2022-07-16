"""
I've used the term 'object' a lot so far - you may have even read that everything in Python is an object. What does that mean?
In short, objects carry some things around with them. You access that stuff using Python's dot syntax.
For example, numbers in Python carry around an associated variable called imag representing their imaginary part.
(You'll probably never need to use this unless you're doing some very weird math.)

"""

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

help(x.bit_length())

planet = ["Mercury", "Pluto", "Earth", "Mars", "Venus"]

# append adds a value to the end of the list
print(planet)

# pop removes and returns the last value of the list
print(planet.pop())
print(planet)

# returns the index number of the value which Earth is in the list
print(planet.index("Earth"))

# Using bools with list
print("Mars" in planet)
print("mercury" in planet)  # returns false due to case sensitivity

