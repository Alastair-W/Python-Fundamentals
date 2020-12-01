import random

def randint(min=0, max=100):
    if min > max:
        return 'Min has to be less than Max'
    else:
        num = random.random() * (max-min) + min
        return num

print(randint(min=50, max=5))