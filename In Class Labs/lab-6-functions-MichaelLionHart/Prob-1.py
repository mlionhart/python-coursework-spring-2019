# Prob-1.py

def function1(a, b):
    if a < 10:
        return -2
    elif a > 10:
        return 2
    elif b < 5:
        return -1
    elif b > 5:
        return 1
    else:
        return 0


def unitTest():
    print("Running unit tests\n")
    print("Test 1: a = 8, b = 0, expected value: -2, actual value:", function1(8, 0))
    print("Test 2: a = 12, b = 0, expected value: 2, actual value:", function1(12, 0))
    print("Test 3: a = 10, b = 3, expected value: -1, actual value:", function1(10, 3))
    print("Test 4: a = 10, b = 6, expected value: -1, actual value:", function1(10, 6))
    print("Test 5: a = 10, b = 5, expected value: 0, actual value:", function1(10, 5))
    # your code below here

    print()


if __name__ == "__main__":
    unitTest()        