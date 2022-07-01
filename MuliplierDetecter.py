'''
Python Practice problem 8 (Easy, 10 points)
Rohit Is A Fraud
Rohit is a fraud by nature.
Rohit wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.
Rohit did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.
Your function should be able to find out the wrong values in Rohan’s table and expose Rohit as a fraud.
Note: Rohit function returns a list of numbers like this
Rohit Function Input:
rohitMultiplication(6)
Rohit function returns this output:
[6, 12, 18, 26, …., 60]
You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None.
'''
import random

def rohitMultiplication(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table

def isCorrect(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i-1

    return None

if __name__ == "__main__":
    # print(rohitMultiplication(7))
    number = int(input("Enter a number: "))
    myTable = rohitMultiplication(number)
    print(myTable)

    wrongIndex = isCorrect(myTable, number)
    print(f"The table is wrong at index {wrongIndex + 1} ") #----> (As index Starts From Zero)