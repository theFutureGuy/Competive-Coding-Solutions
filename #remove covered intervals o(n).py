#remove covered intervals o(n)
l = [[1,8],[3,6],[2,8]]

#optimal sol to merge the array and return lists remaining after removal of unnessary lists
l.sort(key = lambda i:(i[0],i[-1]))

res = [l[0]]
for l,r in l[1:]:
    prevL,preR = res[-1]

    if prevL <= l and preR >=r:
        continue
    res.append([l,r])

print(res)
