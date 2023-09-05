#print only one subsequence whose sum is k using Recursion

def f(i,n,nums,sum,arr,s):
    if(i==n):
        if(s==sum):
           print(nums)
           return True
        else:
            return False
        

    #take condition, take the element into subsequence
    nums.append(arr[i])
    s+=arr[i]
    if(f(i+1,n,nums,sum,arr,s)==True):
        return True
    nums.remove(arr[i])
    s-=arr[i]
    #not take condition, not take the element into subsequence
    if(f(i+1,n,nums,sum,arr,s)==True):
        return True
        
    return False


arr = [1,2,3,4,5,6,7,8,9]
n=9
sum = 15
f(0,n,[],sum,arr,0)
