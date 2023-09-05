def sieveofEratosthenes(num1,num2):
    prime_lst = []
    check_lst = []

    for i in range(2,num2+1):

        if i < num1:
            if i not in check_lst:
                check_lst.append(i)
                for j in range(i*i,num2+1,i):
                    check_lst.append(j)

        else:
            if i not in check_lst:
                prime_lst.append(i)
                for j in range(i*i,num2+1,i):
                    check_lst.append(j)

    return prime_lst

print(sieveofEratosthenes(101,150))
