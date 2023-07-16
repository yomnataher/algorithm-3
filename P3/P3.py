def merge(A, aux, low, mid, high):
    k = i = low
    j = mid + 1
    inversionCount = 0
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i = i + 1
        else:
            aux[k] = A[j]
            j = j + 1
            inversionCount += (mid - i + 1)
        k = k + 1

    while i <= mid:
        aux[k] = A[i]
        k = k + 1
        i = i + 1

    for i in range(low, high + 1):
        A[i] = aux[i]
    return inversionCount
# ----------------------------------------------------------------------------
def mergesort(A, low, high):
    aux = A.copy()
    if high <= low:        
        return 0
        
    mid = (low + high)//2
    inversionCount = 0
    inversionCount += mergesort(A, low, mid)
    inversionCount += mergesort(A, mid + 1, high)
    inversionCount += merge(A, aux, low, mid, high)
    return inversionCount
#--------------------------------------------------------------------------------
#main
N = int(input())
A = list(map(int,input().strip().split()))[:N]
print(mergesort(A, 0, len(A) - 1))