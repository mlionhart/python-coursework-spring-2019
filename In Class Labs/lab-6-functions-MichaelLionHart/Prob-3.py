# Prob-3.py

def main(age):
    if (0 <= age <= 1):
        classification = 'I'
    elif (1 <= age <= 13):
        classification = 'C'
    elif (13 <= age <= 18):
        classification = 'T'
    elif (age >= 18):
        classification = 'A'
    else:
        classification = 'U'
    return classification

def unitTest():
    print('if age is 0 - 1 years old:\t ', main(1))
    print('if age is 1 - 13 years old:\t ', main(6))
    print('if age is 13 - 18 years old:\t ', main(15))
    print('if age is 18 or more years old:\t ', main(72))
    print('if age is outside valid range:\t ', main(-20))

unitTest()
