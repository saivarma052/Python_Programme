#fiboniacci_series

n = int(input("Enter a max number of terms in the fiboniacci series:"))

print("selected values of n is: ", n)
fibonacci_series = []
#first two of series would be start with 0 and 1

n0 = 0
n1 = 1
count = 0
if (n <= 0):
    print("Enter a number which is greater than 1 ")
elif (n == 1):
    print("Fiboniacci series up to", n ,"\n")
else:
    print("Fiboniacci Series:")
    for i in range(n):
        fibonacci_series.append(n0)
        print(n0)
        nth = n0 + n1
        n0 = n1
        n1 = nth
print(fibonacci_series)