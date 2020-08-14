x = [[4, 3], [2, 1]]
y = [[4, 3], [2, 1]]
result = [[0, 0], [0, 0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k]*y[k][j]
for r in result:
    print(r)
