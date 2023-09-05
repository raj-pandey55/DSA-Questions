r1=int(input('Enter rows of 1st matrix'))
c1=int(input('Enter cols of 1st matrix'))

matrix1=[]

for i in range(r1):
    temp=[]
    for j in range(c1):
        temp.append(int(input('Enter elements')))
    matrix1.append(temp)


print(matrix1)

r2=int(input('Enter rows of 2nd matrix'))
c2=int(input('Enter cols of 2nd matrix'))

matrix2=[]

for i in range(r2):
    temp=[]
    for j in range(c2):
        temp.append(int(input('Enter elements')))
    matrix2.append(temp)


print(matrix2)

result=[]
sum=0
if(r1==c2):
    for i in range(r1):
        temp=[]
        for j in range(c2):
            temp.append(int(0))
        result.append(temp)


    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j]=matrix1[i][k]*matrix2[k][j]

    print(result)

    
else:
    print('Matrix Multiplication is not Possible')
      
                
