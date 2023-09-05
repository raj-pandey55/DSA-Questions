#recursive python function to solve the tower of hanoi

def TowerOfHanoi(n, source, destination, auxiliary):
    if n==1:
        print("Move disk 1 to source",source, "to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move Disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)

#driver code

n=3
TowerOfHanoi(n,'A','B','C')
#A, C and B are name of rods
