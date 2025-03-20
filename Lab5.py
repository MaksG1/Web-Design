a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))


if a < b:
    for i in range(a,b):
        print(i)
elif a > b:
    for i in range(a,b-1,-1):
        print(i)

        