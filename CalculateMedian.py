"""
Median
The Median is the middle value among all the values in sorted order.
Here we need to calculate the mid-value of all the values in a dataset.
But before calculating the Median, we need to arrange all the values in sorted order.
There are two different ways of calculating the median value:
"""
# when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
# when the total number of values is odd: Median = {(n+1)/2}thterm

# Median
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 -1]
    median = (m1+m2)/2
else:
    median = list1[len(list1)//2]

print(median)