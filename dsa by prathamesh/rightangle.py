def rightangle(n):
    for i in range(n):   #in outer loop where * will be print
        for j in range(i+1): #the j will check the column for the space and it will be increment till n 
            print("*",end = " ")
        print()
rightangle(5)