# find max and second max of an array

arr = [10,3,45,6,8,42,56,48]

max=min=arr[0]
smin=smax=arr[0]
for num in arr:
    if num>max:
        smax=max
        max=num
    elif (num>smax and num!=max):
        smax=num
    if num < min:
        smin = min
        min = num

print("smallest: ", min)
print("second smallest: ", smin)
print("largest: ", max)
print("second largest: ", smax)