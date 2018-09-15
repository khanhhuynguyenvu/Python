
# Python 3 Program to find sum of  
# Fibonacci numbers in O(Log n) time. 
  
MAX = 1000
  
# Create an array for memoization 
f = [0] * MAX
  
# Returns n'th Fibonacci number 
# using table f[] 
def fib(n) : 
    # Base cases 
    if (n == 0) : 
        return 0
    if (n == 1) : 
        f[n] = 1
        return (f[n]) 
    if (n == 2):
        f[n] = 1
        return (f[n])
  
    # If fib(n) is already computed 
    if (f[n]) : 
        return f[n] 
  
    if( n & 1) : 
        k = (n + 1) // 2
    else :  
        k = n // 2

    # Applyting above formula [Note value n&1 is 1 
    # if n is odd, else 0. 
    if((n & 1) ) : 
        f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) 
    else : 
        f[n] = (2*fib(k-1) + fib(k))*fib(k) 
  
    return f[n] 
  
# Computes value of first Fibonacci numbers 
def calculateSum(n): 
  
    return fib(n+2) - 1
  
# Driver program to test above function 
n = 7
for i in range(0,n+1):
    print(i,' . . ',fib(i))
  
# This code is contributed by 
# Smitha Dinesh Semwal 