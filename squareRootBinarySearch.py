n=100

i=1
j=100
count=0

while(i!=j-1):
    mid = i + (j-i)//2

    i = mid

    count+=1

print(count)
