n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
n3 = int(input("Enter number: "))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

factorial_n1 = factorial(n1)
factorial_n2 = factorial(n2)
factorial_n3 = factorial(n3)

print(factorial_n1)
print(factorial_n2)
print(factorial_n3)
