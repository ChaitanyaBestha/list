a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if a>100 and a<999:
    if b>100 and b<999:
        if c>1000 and c<9999:
            print("+"+"("+str(a)+")"+str(b)+"-"+str(c))
        else:
            print("enter valid data") 
    else:
        print("nooo")
else:
    print("enter valid data")