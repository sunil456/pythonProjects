"""
The execution or running time of the program indicates how quickly the output is delivered based
on the algorithm you used to solve the problem. To calculate the execution time of the program,
we need to calculate the time taken by the program from its initiation to the final result.
"""

"""
So to calculate the execution time of a Python program, we need to follow the steps mentioned below:
1. First, store the time of initiation of the program into variable;
2. Write the python program;
3. Store the end time of the program into a variable;
4. Subtract the time of initiation of the program from the end time of the program;

In the end, you will get the execution time of your program in seconds.
"""

from time import time

start = time()

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a + str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)
