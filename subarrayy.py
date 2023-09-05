def subarray(arr,start,end,n):
  if(end==n):
    return
  
  if(start>end):
    subarray(arr,0,end+1,n)
  else:
    temp=[]
    for i in range(start,end+1):
      temp.append(arr[i])
    print(temp)
    subarray(arr,start+1,end,n)

arr = [1,2,3,4]
n=4
subarray(arr,0,0,n)