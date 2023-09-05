#Memoization
def f(n,dp):
    if(n<=1):
        return n
    if(dp[n]!=-1):
        return dp[n]
    dp[n] = f(n-1,dp) + f(n-2,dp)
    return dp[n]

n=5
dp = [-1]*(n+1)
print(f(5,dp))

#tabulation
dp=[0,1]
n=5
for i in range(2,n+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[n])

#space optimization
prev = 1
prev2 = 0
n=5
for i in range(2,n+1):
    curri = prev + prev2
    prev2 = prev
    prev = curri

print(prev)    