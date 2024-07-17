n = int(input("Enter a number: "))

print("you entered fib number is:", n)

fibonaccinum = []

n0 = 0
n1 = 1
i = 0
if n <= 0:
    print("Enter an integer value greater than 2")

elif n == 1:
    print("Enter the upto: ", n)

else:
    print("Fibonacci series is:")
    while i < n:
        fibonaccinum.append(n0)
        print(n0)
        nth = n0 + n1
        n0 = n1
        n1 = nth
        i +=1
print(fibonaccinum)

