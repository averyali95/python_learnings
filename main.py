"""This is how you define a function in python """
def least_differences(num1, num2, num3):
    diff1 = num1 - num2
    diff2 = num2 - num3
    diff3 = num1 - num3
    return min(abs(diff1), abs(diff2), abs(diff3))

"""Within a print function, you can add a seperator using sep=("seperator symbol")"""
print(
    least_differences(1, 5, 9),
    least_differences(2, 4, 11),
    least_differences(3, 6, 9), sep=(",")
)
"""Round the first number to the 2nd decimal place"""
print(round(3.212112, 2))
print(round(392039397, -4))

"""Return the number of leftover candies that must be smashed after distributing
the given number of candies evenly between 3 friends.
When we set num_of_friends = 3, it will default the value of three if there is no value inputed as an arg
>>> to_smash(91)
1
"""
def to_smash(total_candies, num_of_friends=3):
    return total_candies % num_of_friends

print(to_smash(102))