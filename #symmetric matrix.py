#symmetric matrix

l = [[1],[2,3],[4,5,6],[7,8,9,10]]

# [1]
# [2 3]
# [4 5 6]
# [7 8 9 10]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        l[i].append(l[j][i])


print(l)

 

