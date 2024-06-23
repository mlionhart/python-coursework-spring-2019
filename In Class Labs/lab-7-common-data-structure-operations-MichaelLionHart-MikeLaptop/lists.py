# lists.py

# general instructions: 
#   - print a blank line between sections of output
#   - Add your comments using triple quotes. Example:
''' student comment'''

def main():
    '''
    - creation
    '''
    # create an empty list using the variable name "l1" and print it
    l1 = []
    print(l1)

    # create a list with 3 elements using the variable name "l2". The elements
    # should be an int, a float and a string. Print l2
    l2 = [32, .51, 'my age in years, plus months - as a float']
    print(l2)


    '''
    - element access
    - traversal
    '''
    # this next section demonstrates both access and traversal
    # write a for loop that prints out the elements of l2, each on a 
    # separate line.
    # DO NOT hard code the stop value - use len()
    # your code should use indexing
    # the line should contain the value of the index as well as the element
    for i in range(len(l2)):
        x = print('position', i, ': ', l2[i])
    print()

    # repeat the loop but use l2 itself as the sequence. In this case index
    # values will not be available, so just print the elements
    for i in l2:
        x = print(i)
    print()

    '''
    - element insertion
    '''
    # mutable sequences like lists have two mechanisms to insert a new value.
    # use append() to add a new element to the end of l2 and print l2
    l2.append('new element')
    print(l2)
    print()
    

    # use insert to add a new element at the beginning of l2 and print l2.
    l2.insert(0, 'new element 2')
    print(l2)

    '''
    - element updates
    '''
    # use indexing and assignment to change the second element of l2 to 999
    l2[1] = 999
    print()

    # print l2
    print(l2)
    print()


    '''
    - element deletion
    '''
    # delete item 4 from l2 and print l2
    l2.pop(3)
    print(l2)
    print()


    '''
    - search
    '''
    # given the list
    l = ['a', 'e', 'i', 'o', 'u']
    # use the index() method to find the index of 'i'
    # print the index
    print("index of l: ", l.index('i'))
    print()


    '''
    - sort
    '''
    # When lists have elements of the same type it is sometimes useful to 
    # sort them. see: https://docs.python.org/3/library/stdtypes.html#lists

    # given the list
    l = [-3, 99, 0, -451, 1234]
    # sort the list and print it
    l.sort()
    print(l)
    print()

    # sort in the reverse order and print it
    l.reverse()
    print(l)

main()