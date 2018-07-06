import random

# generate random list of 20 numbers from 0-49
random_numbers = [random.randint(0,50) for i in range(20)]

print(random_numbers)

# generate a new list were each item is the square
# of the number generated earlier
random_squared = [x * x for x in random_numbers]

print(random_squared)