""" , define a function called sign which takes a numerical argument and returns -1 if it's negative,
 1 if it's positive, and 0 if it's 0."""

def sign(number):
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0

""" We have to cast the input to an integer data value so it can be passed into the function"""

user_input = int(input("Please enter a number: "))
print(sign(user_input))


def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    """
    if total_candies == 1:
        print("Splitting 1 candy")
    else:
        print("Splitting", total_candies, "candies")
    """ Or you can write the conditional inside of the print statement"""
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")


to_smash(91)
to_smash(1)
""" More boolean functions. Below -> First function is the long way, second function does the same thing in less lines of code"""
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0

print(is_negative(-2))
print(concise_is_negative(-2))
"""
The boolean variables ketchup, mustard and onion represent whether a customer wants a particular topping on their hot dog. We want 
to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. For example:
"""
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

print(onionless(True, True, False))
print(onionless(True, True, True))
print(wants_all_toppings(True, True, False))
print("All toppings: " + str(wants_all_toppings(True, True, True)))

""" This condition would be pretty complicated to express using just and, or and not, but using boolean-to-integer conversion gives us this 
short solution:

return (int(ketchup) + int(mustard) + int(onion)) == 1
Fun fact: we don't technically need to call int on the arguments. Just by doing addition with booleans, Python implicitly does the integer conversion. So we could also write...

return (ketchup + mustard + onion) == 1 """
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    """return (int(ketchup) + int(mustard) + int(onion)) == 1 """
    return (ketchup + mustard + onion) == 1

