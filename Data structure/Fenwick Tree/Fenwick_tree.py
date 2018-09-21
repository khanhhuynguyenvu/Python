def update(bt,n,i,val):
    #Index in Bit tree begin from 1
    i+=1
    while(i<=n):
        bt[i]+=val
        i+=(i&-i)
def getsum(bt,i):
    #Index in Bit tree begin from 1
    i+=1
    Sum = 0
    while(i>0):
        print(i,' ',bt[i])
        Sum+=bt[i]
        i-=(i&-i)
    return Sum
def initBitTree(arr):
    n = len(arr)
    BitTree = [0]*(n+1)
    for i in range(n):
        update(BitTree,n,i,arr[i])
    return BitTree
#Main
arr = [5,-1,3,4,-1]
res = initBitTree(arr)
#r = int(9)
#rint("Sum from [0] to [",r,"] = ",str(getsum(res,r)))
for i in range(len(arr)):
    t = getsum(res,i)
    print('---')