from collections import deque


row = [ -1, 0, 1, 0]
col = [ 0, 1, 0, -1]
 

def isValid(vis, row, col):
    if (row < 0 or col < 0 or row >= 4 or col >= 4):
        return False
    if (vis[row][col]):
        return False
    return True
 
def BFS(grid, vis, row, col):
    q = deque()
    q.append(( row, col ))
    vis[row][col] = True

    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end = " ")

        for i in range(4):
            adjx = x + row[i]
            adjy = y + col[i]
            if (isValid(vis, adjx, adjy)):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True
 
# Driver Code
if __name__ == '__main__':
    grid= [ [ 1, 2, 3, 4 ],
           [ 5, 6, 7, 8 ],
           [ 9, 10, 11, 12 ],
           [ 13, 14, 15, 16 ] ]
 
    vis = [[ False for i in range(4)] for i in range(4)]
 
    BFS(grid, vis, 0, 0)