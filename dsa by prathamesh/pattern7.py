rows = 5

# Upper half (including the middle row)
for i in range(1, rows + 1):
    spaces = "  " * (rows - i)
    stars = " ".join(["*"] * (2 * i - 1))
    print(spaces + stars)

# Lower half
for i in range(rows - 1, 0, -1):
    spaces = "  " * (rows - i)
    stars = " ".join(["*"] * (2 * i - 1))
    print(spaces + stars)