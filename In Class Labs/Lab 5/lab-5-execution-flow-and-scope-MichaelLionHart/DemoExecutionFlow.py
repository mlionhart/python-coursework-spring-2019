# DemoExecutionFlow.py
# The "Happy Birthday" song

def happy():
    print("Happy birthday to you!")

def sing(person):
    happy()
    happy()
    print("Happy birthday, dear", person + '.')
    happy()

def main():
    name = input("Enter a name: ")
    sing(name)
    print()
    name = input("Enter another name: ")
    sing(name)

main()    