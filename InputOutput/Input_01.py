n,m = map(int,input().split())
arr = [int(x) for x in input().split()]
sum = 0
for i in range(0,n):
    sum+=arr[i]
    
print('Dap an:',str(sum))
print('Array: ',arr)
print('n = ',n)
print('m = ',str(m))
