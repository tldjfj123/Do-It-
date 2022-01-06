def max3(a, b, c) :
    maximum = a
    if b > maximum :
        maximum = b
    if c > maximum :
        maximum = c
        
    return maximum

print(max3(3, 2, 1))
print(max3(3, 1, 2))
print(max3(2, 3, 1))
print(max3(1, 2, 3))


