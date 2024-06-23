# Prob-2.py
def fibonacci(n): 
    if n < 0:
        print('invalid input')
    a, b = 0, 1
    for i in range(n):
        print(b, end=' , ')
        a, b = b, a+b

def unitTest():
    print()
    print('With a sequence of 6: ')
    fibonacci(6)
    print()
    print('With a sequence of 3: ')
    fibonacci(3)
    print()
    print('With a sequence of 22: ')
    fibonacci(22)
    print()
    print('With a sequence of 12: ')
    fibonacci(12)

unitTest()