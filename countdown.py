from numpy import sort


n = 4
dis = [3,2,4,1]
t = [2,0,1,4]
T = 46

d={}
count = 0
d = {}
for i in range(len(dis)):
    d[dis[i]] = t[i]
    sorted(d.keys())
    for i in d:
        if d.items()<=T :
            count+=1
            T-=d.items()
print(count)