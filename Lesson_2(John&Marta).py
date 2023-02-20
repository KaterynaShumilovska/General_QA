#Task_1
john_salary = float(2500)
marta_salary = float(2100)

print("Salary:", john_salary)
print("Salary:", marta_salary)

#Task_2
john_age = int(29)
marta_age = int(25)

print("Age:", john_age)
print("Age:", marta_age)

#Task_3
john_name = str("John")
marta_name = str("Marta")

print("Name:", john_name)
print("Name:", marta_name)

#Task_4
john_gender = None
marta_gender = 12

print("Gender:", bool(john_gender))
print("Gender:", bool(marta_gender))

#Task_5
john_friends = ['Peter', 'Josh', 'Amelia', 'Anthony', 'Marta']
marta_friends = ['Zoe', 'Julia', 'Amelia', 'Philip', 'John']

#Task_6
people = ['Noah', 'Liam', 'Mason', 'Anthony', 'Ethan', 'Liam','William', 'Michael', 'Anthony', 'Liam']
people_uni = set(people)

print(people_uni)

#Task_7
j_geo_coordinates = (46.4825, 30.7233)
m_geo_coordinates = (50.4547, 30.5238)


#Task_8
john_info = {'Full_name': 'John Johnson',
             'Age': john_age,
             'Salary': john_salary,
             'Gender': bool(john_gender),
             'Friends': john_friends,
             'Coordinates': j_geo_coordinates}
marta_info = {'Full_name': 'Marta Thompson',
             'Age': marta_age,
             'Salary': marta_salary,
             'Gender': bool(marta_gender),
             'Friends': marta_friends,
             'Coordinates': m_geo_coordinates}
print(john_info)
print(marta_info)
