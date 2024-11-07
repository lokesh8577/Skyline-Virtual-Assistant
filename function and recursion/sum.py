def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

n = int(input("enter the value of n : "))
print(sum(n))