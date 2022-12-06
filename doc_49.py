a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
i=0
while i<len(a):
    if a[i]=='f':
        b=i
    elif a[i]=='c':
        s=i
    elif a[i]=='k':
        d=i
    elif a[i]=='w':
        e=i
    i=i+1
print("Last occurrence of f in the said list:",b)                    
print("Last occurrence of c in the said list:",s) 
print("Last occurrence of k in the said list:",d) 
print("Last occurrence of w in the said list:",e) 