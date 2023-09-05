#count subsequences whose sum is k using recursion

def f(i,n,sum,arr,s):
    if(i==n):
        if(s==sum):
           return 1
        else:
            return 0
        

    #take condition, take the element into subsequence
    
    s+=arr[i]
    l=f(i+1,n,sum,arr,s)
    
    s-=arr[i]
    #not take condition, not take the element into subsequence
    r=f(i+1,n,sum,arr,s)
        
    return l+r


arr = [1,2,3,4,5,6,7,8,9,]
n=9
sum = 15
print(f(0,n,sum,arr,0))
