#Task 1
from array import *

numbers = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in numbers:
    if i < len(numbers):
        print(i, end=' ')
    else:
        print(i)

j = 1
while j <= len(numbers):
    if j < len(numbers):
        print(j, end=' ')
        j += 1
    else:
        print(j)
        j += 1

#Task 2
var = 10
result = 'True' if (var == 10) else 'False'
print(result)

#Task 3
elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd = []
even = []

for i in range(len(elements)):
    if (i % 2 != 0):
        odd.append((i, elements[i]))
    else:
        even.append((i, elements[i]))

print("List of tuples with odd index:", odd)
print("List of tuples with even index:", even)

#Task 4
friends = ["Marta", "John", "James"]
enemies = ["John", "Johnatan", "Artur"]
new1 = ''
new2 = ''

for i in friends:
    if i == 'James':
        continue
    elif i in enemies:
        new1 += str(i) + ' '
    else:
        new2 += str(i) + ' '

print(f"{new2}we are the best friends")
print(f"{new1}we are not friends anymore")
