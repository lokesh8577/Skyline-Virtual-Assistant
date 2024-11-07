n=int(input("enter the value of n : "))
def facto(n):
   if n==1:
      return 1
       
     
   return n*facto(n-1)
        

print(facto(n))        
