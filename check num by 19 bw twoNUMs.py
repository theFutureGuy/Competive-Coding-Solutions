from math import floor
def chk19(s,e):
    count = 0
    for i in range(s, e):
        if (i % 19 == 0):
            count = count + 1
 
    return count  # o(e) 

#optimised approach using exclusive method:
# x is div by 19 when mod 19 ==0, where x > 19 hence if x < 19 :none is div by 19 but if x > 19 and end range is large time is expensive.
# start = count(start) * 19 
#end  = count(end) * 19
# therefore the totcount can be floor(count(end)/19 + count(start)/19)

def optiChk19(s,e):
    if (s % 19 == 0):
        return (floor((e/19) - (s/19))) + 1
    else:
        return (floor((e/19) - (s/19)))



start = 10
end = 50
 
call1 = chk19(start,end)
call2 = optiChk19(start,end)
print("total no div by 19 : ",call1)
print("total no div by 19 : ",call2)
