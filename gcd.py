
def gcd(a, b):
    # Find minimum of a and b
    result = min(a, b)
 
    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
 
    # Return the gcd of a and b
    return result
 
 
# Driver Code
a = 98
b = 56
 
print(f"GCD of {a} and {b} is {gcd(a, b)}")