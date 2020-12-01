import random

def randint(min=50, max=10):
    if min > max:
        return 'Min has to be less than Max'
    else:
        num = random.random() * (max-min) + min
        return num

print(randint(min=-50, max=-20))