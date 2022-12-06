a = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sumeven=0
sumodd=0
while i<len(a):
    if a[i]%2==0:
        sumeven+=a[i]
    else:
        sumodd+=a[i]
    i=i+1
print("sumeven=",sumeven)
print("sumodd=",sumodd)         

