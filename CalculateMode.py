"""
Mode
Mode is the most frequently occurring value among all the values.
"""

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i] += 1
print(frequency)

frequent = max(frequency.values())
print(frequent)

for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)