""" The for loop specifies

the variable name to use (in this case, planet)
the set of values to loop over (in this case, planets)
You use the word "in" to link them together.

The object to the right of the "in" can be any object that supports iteration. Basically, if it can be thought of as a
 group of things, you can probably loop over it. In addition to lists, we can iterate over the elements of a tuple"""

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')

"""range()
range() is a function that returns a sequence of numbers. It turns out to be very useful for writing loops.

For example, if we want to repeat some action 5 times:
"""

for i in range(5):
    print("Doing important work. i =", i)

"""
while loops
The other type of loop in Python is a while loop, which iterates until some condition is met:
"""

i = 0
while i < 50:
    print(i, end=" ")
    i += 1


def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is
    True if L[i] is greater than thresh, and False otherwise.

    elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """

    greater2 = []
    for num in L:
        if num > thresh:
            greater2.append(True)
        else:
            greater2.append(False)
    """
        or
    for num in L:
        greater2.append(num>thresh)
    return greater2
    """
    return greater2

print(elementwise_greater_than([1, 2, 3, 4], 2))