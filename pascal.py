
num = 5

for i in range(1,num+1):
    for j in range(num-i,0,-1):
        print(" ", end = "")
    

    for k in range(1,(2*i)-1,2):
        print(k,"",end='')
    print("\r")
    
    
