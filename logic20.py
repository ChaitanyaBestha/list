a="my name is chaitu"
b=a.split()
i=0
while i<len(b):
    d=b[i]
    if d=="":
        print(d,end="")
    else:
        print(d)
    i=i+1