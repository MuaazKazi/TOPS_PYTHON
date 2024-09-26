# How can you pick a random item from a list or tuple?

"""
-In Python, I can pick a random item from a list or tuple using the random module.

"""
# Example: 

my_tuple = (1, 2, 3, 4, 5)
random_item = random.choice(my_tuple)
print(random_item)

import random
list=[1,2,3,4,5]
Random_item=random.choice(list)
print("Random element:",Random_item)