# Module 3
#   Programming Assignment 4
#     Prob-5.py

# Mike Hart

def main():
    try:
        x = eval(2)
        print("x:", x)
    except TypeError:
        print('Attempting to evaluate a non-string')
    except:
        print('Something went wrong')

main()