# A list of Numbers
names = ["Sai", "Kiran", "Praveen", "Bala", 'Srinu']
Salary = [2000, 4000, 3000, 6000, 1000]
numbers = [1, 2, 3, 4, 5]

# A list of mixed data types
test_list = [309, "sai", 45.98, True]
print(test_list)

#Modifying a list
names.append("Ganesh")
names.append("Laxman")
names.append("Laxman")
names.append("Laxman")
names.append("Laxman")
names.remove("Sai")
names.extend((["Sathan", "Rishi", "Balaji", "Khanna"]))
Salary.append(6500)
Salary.sort()
names.insert(11, "Laxman")
Last_entry = names.pop()
Salary.sort()
place = names.index("Ganesh")
names.reverse()
Candidates = names.copy()
#print declaration
print(names)
print(Salary)
print('type of number is', type(numbers))
print(names)
print(names)
print(numbers[0:6:2])
print(Salary)
print(names.count("Laxman"))
print(Last_entry)
print(place)
print(names)
print(Candidates)
