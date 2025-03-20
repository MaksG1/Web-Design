num_list = []
while True:
    n = int(input("Enter a number: "))
    if n != 0:
        num_list.append(n)
    elif n == 0:
        break
print(sum(num_list)/len(num_list))