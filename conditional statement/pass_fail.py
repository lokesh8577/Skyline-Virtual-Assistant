marks1=int(input("enter marks1 : "))
marks2=int(input("enter marks2 : "))
marks3=int(input("enter marks3 : "))
percentage = 100*(marks1+marks2+marks3)/300
if(percentage>=40 and marks3>=33 and marks2>=33 and marks1>=33):
    print("you are passed ",percentage)

else:
    print("you are failed ",percentage)

print("thank you")