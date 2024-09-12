def greater_value(n1,n2,n3):
    if n1 > n2 or n1 > n3:
        print("n1 is greater value")
        if n1 == n2:
            print("n1 is equal to n2")
            if n1 > n3:
                print("n1 and n2 are equal and greater than n3")
    elif n2 > n1 or n2 > n3:
        print("n2 is greater value")

    else:
         print("n3 is greater value")


n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))
n3 = int(input("Enter a third number: "))

print(greater_value(n1,n2,n3))
print("Greater Value is:",)