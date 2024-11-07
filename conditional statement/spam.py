p1='make a lot money'
p2='click this'
p3='buy now'
p4='suscribe this'
comment = input("enter commnet  : ")
if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("commment is spam")

else:
    print("comment is not spam")
    