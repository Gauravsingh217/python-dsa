def right_aligned_triangle(n):
    for i in range(1, n + 1):  # outer loop for rows
        for j in range(5, 5 - i, -1):  # inner loop for columns
            print(j, end=" ")
        print()