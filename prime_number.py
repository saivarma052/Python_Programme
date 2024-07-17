Number = 25
def is_prime(n):
    count = 0
    if n > 1:
        for i in range(1, n + 1):
            if (n % i) == 0:
                count = count + 1
    if count == 2:
        return True
        print("It is a Prime")
    else:
        return False
        print("Number is not Prime")


### Below code is correct
# if is_prime(Number):
#     print("It is a prime number")
# else:
#     print("It is not a prime number")
### Above code is correct

num = int(input("Enter a number: "))  # num= 5

Test_Prime_List = []

for i in range(0, num):
    Test_Prime_List.append(i)

print(Test_Prime_List)

for j in range(0, len(Test_Prime_List)):
    n = Test_Prime_List[j]
    check = is_prime(n)
    if check == True:
        print(f"{n} is  Prime")
    else:
        print(f"{n} is  not a Prime")

    # print(check)
    #
    # if check is True:
    #     l = Test_Prime_List[j]
    #     print(f"{l} is a Prime", l)
    # else:
    #     m = Test_Prime_List[j]
    #     print(f"{m} is Prime", m)

#   print(test[x])
#
# # for i in range(1, num+1):
# #     listed_value.append(i)
# #     s = listed_value[i]
# #     print(s)
# #
# #
# # # for i in range(i, num):
# # #     print("I am here")
# # #
# # #     if is_prime(listed_value[i]):
# # #         print(f"{listed_value[i]} is a prime number")
# # #     else:
# # #         print(f"{listed_value[i]} is not a prime number")
# # #
# # #
