# Module 8
#   Programming Assignment 11
#     Prob-2.py
# Mike Hart


class Student(object):
    def __init__(self, name, ID, major, GPA):
        self._name = name
        self._ID = ID
        self._major = major
        self._GPA = GPA
    
    def get_name(self):
        return self._name
    
    def get_ID(self):
        return self._ID
    
    def get_major(self):
        return self._major
    
    def get_GPA(self):
        return self._GPA
    
    def set_name(self, name):
        self._name = name

    def set_ID(self, ID):
        self._ID = ID
    
    def set_major(self, major):
        self._major = major

    def set_GPA(self, GPA):
        self._GPA = GPA

    def Student_print(self):
        print('Name: ' + self._name, end="\t\t")
        print('ID: ' + str(self._ID), end="\t\t")
        print('Major: ' + self._major, end="\t\t")
        print('GPA: ' + str(self._GPA), end="\t\t")


def test():
    studentOne = Student("Joe Bella ", 9933, "Web Development ", 3.8)
    studentTwo = Student("Tucker Blank ", 3399, "Nursing  ", 3.0)
    studentThree = Student("Gayle Ujifusa ", 1011, "Baking   ", 2.8)
    studentFour = Student("Edna Anker ", 9875, "Medical Office  ", 3.0)
    roster = [studentOne, studentTwo, studentThree, studentFour]
    for item in range(4):
        roster[item].Student_print()
        print()
    for item in range(4):
        roster[item].set_name(input("Please enter the student's name: "))
        roster[item].set_ID(input("Please enter the student's ID number? "))
        roster[item].set_major(input("Please enter the student's major? "))
        roster[item].set_GPA(input("Please enter the student's GPA? "))
    for item in range(4):
        roster[item].Student_print()
        print()
test()
