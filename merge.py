arr1=[1,3,5,7]
arr2=[0,2,4,6]
arr3=[]
# n1=int(input())

# for i in range(0,n1):
#   temp=int(input())
#   arr1.append(temp)

# n2=int(input())

# for i in range(0,n2):
#   temp=int(input())
#   arr2.append(temp)

j=0
k=0

while(1):
  if(len(arr3)!=len(arr1)+len(arr2)):
    if(arr1[j]>arr2[k]):
      arr3.append(arr1[j])
      j+=1
    else:
      arr3.append(arr2[k])
      k+=1
  break


for i in range(0,(len(arr1)+len(arr2))):
  print(arr3[i])
