print("please enter your list:")
A =list(map(int,input().strip().split()))
x = len(A)
flag = False
for i in range(x):
     if A[i] > 0:
         flag = True
         break
if not flag:
    M = 0
elif x == 0:
    print("Your list is empty")
elif x == 1:
    print("The maximum sum is ", A[0])
else :
    M = max(A[0],A[1])
    A[1] = M
    for i in range (2,x):
        M = max(A[i-2]+A[i],M)
        M = max(A[i],M)
        A[i] = M
print("The maximum sum is ", M)