wokt = [2, 34, 56, 21, 62, 93, 2, 12, 56]
for i in range(len(wokt)):
    for j in range(len(wokt)):
        if i != j and wokt[i] == wokt[j]:
            break
    else:
        print(wokt[i], end=' ')