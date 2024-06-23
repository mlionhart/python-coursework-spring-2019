# Module-4-Lab-6-Functions

## This Lab has 3 separate parts
____

## Lab 6 Problem 1

**Goals**

- Hone code analysis skills
- Write complete set of unit tests for a function

**Instructions**

1. Analyze the code in Prob-1.py. How many paths through the code are there?
2. A suggested strategy for answering the question: Count how many clauses or conditional code blocks there are
3. The goal is to complete test the function. This means we want to test each possible branch. To do this we need to figure out what inputs test a particular branch. Let's analyze the first clause :
    - what range of values of **a** will trigger the return of -2?
    - what range of values of **b** are possible?
4. You can continue this analysis by filling in the following table:
    | Return value  | Value range for **a** | Value range for **b** |
    | --- | --- | --- |
    | return -2 | | |
    | return 2 | | |
    | return -1 | | | 
    | return 1 | | |
    | return 0 | | |
    | | | | |

5. Now you have the info you need to write your test case code.
6. Fill in your code where indicated in the Python file.
7. Commit and push your updates

____

## Lab 6 Problem 2

**Instructions**

Write a function that outputs the fibonacci series.

The fibonocci series is a series of numbers in which the next number in the series is the sum of the two preceeding numbers. The first few numbers in the series are:  
    `1, 1, 2, 3, 5, 8, ...`    
The next number in the sequence is 5 + 8 = 13

A reference is: https://en.wikipedia.org/wiki/Fibonacci_number

**Specification**

- The function should take a parameter that specifies the number of positions to output. For example, a value of 4 would output the first 4 values in the series.
- The output should be on a single line
- The numbers should be separated by a comma and a space.
- An input value of 0 or less will result in the printing of an informative message.
- Write unit test code to show that your function works as specified.
- The function should return the sum of the values printed.
____

## Lab 6 Problem 3

**Instructions**

Write a function that returns a single character indicating an age classification.

**Specifications**

- The function should take a single numeric parameter indicating age
- The function should return one of the following:

    - 'I' for infant, age 0 - 1 years old
    - 'C' for child, age older than 1 but younger than 13
    - 'T' for teenager, age 13 - 18 years old
    - 'A' for adult, age 18 or older
    - 'U' for unknown, age outside valid range.

- Write test code to thorough test your function

