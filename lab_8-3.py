"""


*** You must write a comment for every chunk of code you write from now on along with your author tag***
Create a Python file named lab_8-3.py
Write the while-loop version of the following for-loop program.

def sum_to(n):
  total = 0
	for i in range(n+1):
		total += i
	return total

The function should be able to have an integer passed to it and return the sum of all the values from 1 to that integer
"""
def sum_to(n):
    
    # Initialize variables
    total = 0
    i = 1

    # Use a while loop to iterate through numbers until "i" is larger than "n"
    while i <= n:
        total += i
        i += 1

    return total

# Find the result of the function through an example
result = sum_to(5)
print(f"The sum of values from 1 to 5 is: {result}")