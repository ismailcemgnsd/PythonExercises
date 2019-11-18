print("Enter three integers")
a = eval(input())
b = eval(input())
c = eval(input())
'''
if a < b and a < c:
    min = a
    if b < c:
        min2 = b
        min3 = c
    else:
        min2 = c
        min3 = b
if b < a and b < c:
    min = b
    if a < c:
        min2 = a
        min3 = c
    else:
        min2 = c
        min3 = a
if c < a and c < b:
    min = c
    if a < b:
        min2 = a
        min3 = b
    else:
        min2 = b
        min3 = a

print(min, min2, min3)
'''

if b < a or c < a:
    if b < a:
        a , b = b , a
    if c < a:
        a , c = c , a

if c < b:
    b , c = c , b

print(a, b, c)


