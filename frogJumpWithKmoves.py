def f(heights,i,dp,k):
  if(i==0):
    return 0
        
  if(dp[i]!=-1):
    return dp[i]
  
  minJumps = 999999999
  for j in range(1,k+1):
    if(i-j>=0):
      jumps= f(heights,i-j,dp,k) + abs(heights[i]-heights[i-j])
      minJumps = min(jumps,minJumps)

  dp[i] = minJumps

  
  return dp[i]

heights = [10,20,30,10]
n=len(heights)
dp = [-1]*(n)
k=4
print(f(heights,n-1,dp,k))

    