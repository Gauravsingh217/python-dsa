rows = 5

# upper part
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    
    spaces = 2 * (rows - i)
    for s in range(spaces):
        print(" ", end=" ")
        
    for k in range(i):
        print("*", end=" ")
    print()

# lower part
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
        
    spaces = 2 * (rows - i)
    for s in range(spaces):
        print(" ", end=" ")
        
    for k in range(i):
        print("*", end=" ")
    print()