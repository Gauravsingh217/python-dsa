def square(n):
    for i in range(n):  #outer loop will be print the rows
        for j in range(n):  #inner loop will be print the columns 
            print("*", end = " ")  #this will be print the stars
        print()
print(square(5))