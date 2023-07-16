def delete(l, r, a):
    if l > r:
        return 0
    counter = 0
    mn_index = l
    for i in range(l,r+1):
        if a[i] != 0:
            counter += 1
        if a[i] < a[mn_index]:
            mn_index=i
    mn_element=a[mn_index]
    for i in range(l,r+1):
        a[i]-=mn_element
    if mn_element > counter:
        return counter
    return min(counter,delete(l,mn_index-1,a)+delete(mn_index+1,r,a)+mn_element)

arr = list(map(int,input().strip().split()))
print(delete(0, len(arr)-1, arr))