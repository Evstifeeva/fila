wokt = [2, 34, 56, 21, 62, 93, 2, 12, 56]
a = 0
for i in range(len(wokt)):
    for j in range(i + 1, len(wokt)):
        if wokt[i] == wokt[j]:
            a += 1
print(a)