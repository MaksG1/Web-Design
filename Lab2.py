n = int(input("Enter a number: "))
num_list=[]
for i in range(0,n):
    num = int(input("Enter a number: "))
    num_list.append(num)
print(num_list.count(0))