#subsequences using recursion

def f(i,n,nums,arr):
  if(i==n):
    print(nums)
    return
        

    #take condition, take the element into subsequence
  nums.append(arr[i])
  f(i+1,n,nums,arr)
  nums.remove(arr[i])
    #not take condition, not take the element into subsequence
  f(i+1,n,nums,arr)
        


arr = [1,2,3]
n=3
f(0,n,[],arr)