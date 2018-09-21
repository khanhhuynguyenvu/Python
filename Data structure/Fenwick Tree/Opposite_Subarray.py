#Counting all pairs got a[i]>a[j] with i<j
N = -10**9-7
arr = [4,6,2,5]
n = len(arr)
new = [N]
#Fuction
def update(Bit,x):
    while(x<=n):
        Bit[x]+=1
        x+=(x&-x)
def get(Bit,x):
    res = 0
    while(x>0):
        res+=Bit[x] 
        x-=(x&-x)
    return res
#
for i in arr:
    new.append(i)
    new.append(i-1)
new.sort()
idx={}
for i,j in enumerate(new):
    idx[j] = i
n = len(new)
#print(new)
ans = 0
Bit = [0 for i in range(n+1)]
for i in arr[::-1]:
    ans+=get(Bit,idx[i-1])
    update(Bit,idx[i])
print(ans)