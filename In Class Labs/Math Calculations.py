# Mike Hart
# LAB 3: Use of the Math Library

# Import Math Library
from math import *

# V = (4/3)pi(r^3)
r = 3
v = (4/3)*pi*(r**(1/3))

# A = 4pi(r^2)
A1 = 4*pi*(sqrt(r))

# slope
y1 = 6
y2 = 5
x1 = 1
x2 = 2
slope = (y2 - y1)/(x2 - x1)

# s = (a+b+c)/2
a = 1
b = 2
c = 3
s = (a+b+c)/2

# A = (s(s-a)(s-b)(s-c))^(1/2)
A2 = sqrt(s*(s-1)*(s-2)*(s-3))

# Results
print("v = ",v)
print()
print("A1 = ",A1)
print()
print("The slope is: ", slope)
print()
print("s = ", s)
print()
print("A2 = ",A2)

mike = 'shut up'
print('I need you to {mike}')
