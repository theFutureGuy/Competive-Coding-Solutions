#triangle 

# arr = [[2],
#        [3,4],
#        [6,5,7],
#        [4,1,8,3]]
arr = [[-10]]
temp = []

if(len(arr) <= 1):
    print(arr)

for i in range(len(arr)):
    # for j in range(len(arr[i])):
    #     if(len(arr[i]) == 1):
    #         temp.append(arr[i][j])
    temp.append(min(arr[i]))
    
print("the min path for triangle : ",sum(temp))