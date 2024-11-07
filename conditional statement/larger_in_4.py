a=int(input("enter first number : "))
b=int(input("enter secound number : "))
c=int(input("enter third number : "))
d=int(input("enter fourth number : "))

if(a>b and a>c and a>d):
    print(str(a)+" is largest")

elif(b>a and b>c and b>d):
    print(str(b)+" is largest")

elif(c>a and c>b and c>d):
    print(str(c)+" is largest")

elif(d>a and d>b and d>c):
      print(str(d)+" is largest")

else:
     print("no one largest")
   

print("thank you for use my program")