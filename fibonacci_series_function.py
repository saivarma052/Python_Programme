def is_fibonacci(n):
    n0 = 0
    n1 = 1
    count = 0

    if n <= 0:
        print("Enter a value which is greater than 1 :", n)
    elif n == 1:
        print("Fibonacci series up to:", n)
    else:
        print("Fibonacci Series:")
        for i in range(n):
            fibonacci_series.append(n0)
            print(n0)
            nth = n0 + n1
            n0 = n1
            n1 = nth

    return fibonacci_series

n = int(input("Enter a max number of terms in the fiboniacci series:"))
print("selected values of n is: ", n)
fibonacci_series = []
check = is_fibonacci(n)
print(check)


#for j in range(0,len(fibonacci_series)):
#    num = fibonacci_series[j]

n = int(input("Enter a max number of terms in the fiboniacci series:"))
print("selected values of n is: ", n)
fibonacci_series = []
check = is_fibonacci(n)
print(check)