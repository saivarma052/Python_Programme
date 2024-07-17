def is_factorial(n):
    while n < 0:
        print("Enter a positive integer")
        n = int(input("Enter a number which is greater than 0"))

    result = 1
    for i in range(1, n+1):
        result = result * i

    return result

n = int(input("Enter a positive integer: "))

fact = is_factorial(n)

print(fact)



n = int(input("Enter a positive integer: "))

fact = is_factorial(n)

print(fact)