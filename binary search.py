l = [4,5,3,5,9,1,10]

def binsearch(l, x):
    low = 0
    high = len(l) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
        if l[mid] < x:
            low = mid + 1
        elif l[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
res = binsearch(l,10)
if res != -1:
    print("Element is present at index", str(res))
else:
    print("Element is not present in array")
