#three sum 2 for sorted
l = [1,4,7,11,15,19]
target = 8
ans = []

ptr=0
while(l[ptr] < target):
    d = target - l[ptr]
    if(d in l and d not in ans and d !=l[ptr]):
        ans.append(l[ptr])
        ans.append(d)
    ptr+=1



l2=[5,4,1,10,8]
target = 8
a = []
hashmap = {}

for i in range(len(l)-1):
    d = target - l[ptr]
    if(d in hashmap[d]):
        hashmap.