num_list = []
while True:
    n = int(input("Enter a number: "))
    if n != 0 and n % 2 ==0:
        num_list.append(n)
    elif n == 0:
        break
print(len(num_list))
