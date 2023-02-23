# Task 1
import json

s_names = 'john peter brian Morgan Adam Maria bart'
print(s_names.title())

# Task 2
friends = ["John", "Marta", "James", "Amanda", "Marianna"]
heading = 'Names'
print(heading.center(15, '*'))
for i in friends:
    print(i.rjust(15))

# Task 3
s = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
s = s.replace(' ', '').replace('&&', ' ').replace('&', ' ').replace('=sssss', '').replace(' ', ';')
s_dict = dict(i.split('=')
              for i in s.split(';'))
print(s_dict)

#Task 4
import re
name = ['FirstItem', 'FriendsList', 'MyTuple']

for i in range(len(name)):
    name[i] = re.sub(r'(?<!^)(?=[A-Z])', '_', name[i]).lower()
print(name)