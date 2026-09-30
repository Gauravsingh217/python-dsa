n = int (input("enter a size of array = "))

arr = [ ]

for i in range(n) :
    num = int(input("enter a number = "))
    arr.append(num)

arr.sort()

print("smallest no = ", arr[0])
print("second smallest = ", arr[1])
print("largest no = ", arr[n-1])
print("second largest = ", arr[n-2])