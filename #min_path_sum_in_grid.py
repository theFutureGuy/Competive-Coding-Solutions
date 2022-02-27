#min_path_sum_in_grid
grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]

row , cols = len(grid),len(grid)

res = [[float("inf")]* (cols+1) for i in range(row+1)] 

res[row-1][cols] = 0

for i in range(row-1,-1,-1):
        for j in range(cols-1,-1,-1):
                print(res[i][j]," ", grid[i][j]," ",res[i+1][j] ," ",res[i][j+1])
                res[i][j] = grid[i][j] + min(res[i+1][j] , res[i][j+1])
                print("after")
                print(res[i][j]," ", grid[i][j]," ",res[i+1][j] ," ",res[i][j+1])

print(res)
print(res[0][0])