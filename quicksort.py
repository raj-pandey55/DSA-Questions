def part(arr,low,high):
    pivot = arr[low]
    i=low
    j=high
    while(i<j):

        while(arr[i]<=pivot and i<=high-1):
            i+=1
        while(arr[j]>pivot and  j>=low+1):
            j-=1

        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]

    arr[low],arr[j]=arr[j],arr[low]

    return j


def qs(arr,low,high):
    if(low<high):
        partition = part(arr,low,high)
        qs(arr,low,partition-1)
        qs(arr,partition+1,high)


arr=[2,4,5,4,4,3,4,5,3,2,3,7,8,9,7,655,4]
n=len(arr)
qs(arr,0,n-1)
print(arr)