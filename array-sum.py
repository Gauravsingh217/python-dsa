n = int(input("enter the size of an array = "))

arr = [ ]

for i in range(n):
    num = int(input("enter the number = "))
    arr.append(num)

total = 0

for i in range(n):
    total = total + arr[i]

print ("sum = ", total)
