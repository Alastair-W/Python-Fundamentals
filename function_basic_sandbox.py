#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# Answer: y = a() = 1, x = b() = 3, 5, 10