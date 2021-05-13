#
l = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# 2
print("Ordonata ascendent:", sorted(l))
print("Initiala:", l)

# 3
print("Ordonata descendent:", sorted(l, reverse=True))
print("Initiala:", l)

# 4
print("Elemente indecsi pari", l[::2])

# 5
print("Elemente indecsi impari", l[1::2])

# 6
print("Elemente multiplii de 3:", end=" ")
for elem in l:
    if elem % 3 == 0:
        print(elem, end=" ")
print()
