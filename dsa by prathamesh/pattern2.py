def pattern2(n):
    for i in range(1, n + 1):    #outer loop for rows
        for j in range(1, i + 1): #inner loop will be increment the number according to the column
            print(j, end = " ")
        print()
pattern2(5)