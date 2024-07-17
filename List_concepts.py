#Need to apply all list operations

num = int(input("Enter a number: ")) #num= 5

listed_value = []

for i in range(1, num+1):
    listed_value.append(i)

print(listed_value)
#list has to at least 2 elements
if num < 2:
    print("Enter minimum 2 indices")
else:
    #requesting 2 indices from user
    while True:
        print("Enter the indices: ")
        index_1 = int(input("Enter the index1: "))
        index_2 = int(input("Enter the index2: "))
        print(f'Original list{listed_value}')

        if index_1 == index_2 or index_1 < 0 or index_2 <0 or index_1 >= num or index_2 >= num:
            print("Indices values are out of the range")
        else:
            break

    #Reverse the elements at the specific indices

    a = listed_value[index_1]
    b = listed_value[index_2]
    listed_value[index_1] = b
    listed_value[index_2] = a
    print(f'Reversed list{listed_value}')


