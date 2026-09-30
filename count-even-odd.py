n = int(input("enter size of an array = "))

arr = []

for i in range(n):
    num=int(input("enter aa no = "))
    arr.append(num)
even = 0
odd = 0
for i in range(n):
    if arr[i] %2 == 0:
        even += 1
    else:
        odd += 1

print("even count = ", even)
print("odd count = ", odd)
