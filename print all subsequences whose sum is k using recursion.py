#print all subsequences whose sum is k using recursion

def f(i,n,nums,sum,arr,s):
    if(i==n):
      if(s==sum):

        print(nums)
      return
        

    #take condition, take the element into subsequence
    nums.append(arr[i])
    s+=arr[i]
    f(i+1,n,nums,sum,arr,s)
    nums.remove(arr[i])
    s-=arr[i]
    #not take condition, not take the element into subsequence
    f(i+1,n,nums,sum,arr,s)
        


arr = [1,2,3,4,5,6,7,8,9,]
n=9
sum = 15
f(0,n,[],sum,arr,0)